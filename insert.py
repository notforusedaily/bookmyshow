import psycopg2
from urllib.parse import urlparse

# Replace this with your PostgreSQL URL
postgres_url = 'postgresql://nullclassintern_user:fE1KkiyLeDXAcueeB6rFnezF5mdiZKux@dpg-cubrcgt2ng1s73arnv50-a.oregon-postgres.render.com/nullclassintern'

# Parse the PostgreSQL URL
url = urlparse(postgres_url)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    database=url.path[1:],  # Remove leading slash
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# Create a cursor object using the connection
cursor = conn.cursor()

# Truncate existing tables
cursor.execute("TRUNCATE TABLE auth_user CASCADE")
cursor.execute("TRUNCATE TABLE movies_theater CASCADE")
cursor.execute("TRUNCATE TABLE movies_seat CASCADE")
cursor.execute("TRUNCATE TABLE movies_movie CASCADE")

# Sample data for movies_movie table
movies_movie_data = [
    (1, 'Avatar', 'image1.jpg', 4.5, 'Actor 1, Actor 2', 'A great movie'),
    (2, 'Openheimer', 'image2.jpg', 4.0, 'Actor 3, Actor 4', 'An exciting movie'),
    (3, 'Barbie', 'image3.jpg', 3.5, 'Actor 5, Actor 6', 'A funny movie'),
    (4, 'Fight_Club', 'image4.jpg', 4.8, 'Actor 7, Actor 8', 'A thrilling movie'),
    (5, 'Gone_Girl', 'image5.jpg', 4.2, 'Actor 9, Actor 10', 'A dramatic movie'),
    (6, 'Transformers', 'image6.jpg', 4.3, 'Actor 11, Actor 12', 'A royal adventure')
]

# Insert data into movies_movie table
for data in movies_movie_data:
    cursor.execute("""
        INSERT INTO movies_movie (id, name, image, rating, "cast", description)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, data)

# Sample data for movies_theater table
movies_theater_data = [
    (1, 'Theater One', '2024-12-27 10:00:00+00', 1),
    (2, 'Theater Two', '2024-12-27 11:00:00+00', 2),
    (3, 'Theater Three', '2024-12-27 12:00:00+00', 3),
    (4, 'Theater Four', '2024-12-27 13:00:00+00', 4),
    (5, 'Theater Five', '2024-12-27 14:00:00+00', 5),
    (6, 'Theater Six', '2024-12-27 14:00:00+00', 6)
]

# Insert data into movies_theater table
for data in movies_theater_data:
    cursor.execute("""
        INSERT INTO movies_theater (id, name, time, movie_id)
        VALUES (%s, %s, %s, %s);
    """, data)

# Create expanded seat data with rows A-H and columns 1-10
# This creates 80 seats per theater (8 rows × 10 columns)
seat_id = 1
movies_seat_data = []

for theater_id in range(1, 7):  # For 6 theaters
    for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        for col in range(1, 11):  # Columns 1-10
            # Mark some seats as booked (around 20% of seats)
            is_booked = False
            if (row == 'B' and col % 4 == 0) or (row == 'E' and col % 3 == 0):
                is_booked = True
                
            seat_number = f"{row}{col}"
            movies_seat_data.append((seat_id, seat_number, is_booked, theater_id))
            seat_id += 1

# Insert data into movies_seat table
for data in movies_seat_data:
    cursor.execute("""
        INSERT INTO movies_seat (id, seat_number, is_booked, theater_id)
        VALUES (%s, %s, %s, %s);
    """, data)

# Commit the transaction
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()

print(f"Database updated with {len(movies_seat_data)} seats across {len(movies_theater_data)} theaters")
