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

# Sample data for auth_user table
# auth_user_data = [
#     (1, 'password1', '2024-12-27 12:00:00+00', True, 'john_doe', 'John', 'Doe', 'john.doe@example.com', True, True, '2024-01-01 10:00:00+00'),
#     (2, 'password2', '2024-12-27 12:00:00+00', False, 'jane_doe', 'Jane', 'Doe', 'jane.doe@example.com', False, True, '2024-02-01 11:00:00+00'),
#     (3, 'password3', '2024-12-27 12:00:00+00', True, 'mark_smith', 'Mark', 'Smith', 'mark.smith@example.com', True, True, '2024-03-01 12:00:00+00'),
#     (4, 'password4', '2024-12-27 12:00:00+00', False, 'lucy_brown', 'Lucy', 'Brown', 'lucy.brown@example.com', False, True, '2024-04-01 13:00:00+00'),
#     (5, 'password5', '2024-12-27 12:00:00+00', True, 'david_jones', 'David', 'Jones', 'david.jones@example.com', True, True, '2024-05-01 14:00:00+00')
# ]

# Insert data into auth_user table
# for data in auth_user_data:
#     cursor.execute("""
#         INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
#     """, data)

# Sample data for movies_booking table

# movies_booking_data = [
#     (1, '2024-12-27 12:00:00+00', 1, 1, 1, 1),
#     (2, '2024-12-27 12:30:00+00', 2, 2, 2, 2),
#     (3, '2024-12-27 13:00:00+00', 3, 3, 3, 3),
#     (4, '2024-12-27 13:30:00+00', 4, 4, 4, 4),
#     (5, '2024-12-27 14:00:00+00', 5, 5, 5, 5)
# ]

# # Insert data into movies_booking table

# for data in movies_booking_data:
#     cursor.execute("""
#         INSERT INTO movies_booking (id, booked_at, user_id, movie_id, seat_id, theater_id)
#         VALUES (%s, %s, %s, %s, %s, %s);
#     """, data)
#Sample data for movies_movie table
movies_movie_data = [
  
   (1, 'Pushapa', 'image1.jpg', 4.5, 'Actor 1, Actor 2', 'A great movie'),
    (2, 'Animal', 'image2.jpg', 4.0, 'Actor 3, Actor 4', 'An exciting movie'),
    (3, 'Saripoda Sinivaram', 'image3.jpg', 3.5, 'Actor 5, Actor 6', 'A funny movie'),
    (4, 'Jailer', 'image4.jpg', 4.8, 'Actor 7, Actor 8', 'A thrilling movie'),
    (5, 'Vikram', 'image5.jpg', 4.2, 'Actor 9, Actor 10', 'A dramatic movie'),
    (6, 'Maharaja', 'image6.jpg', 4.3, 'Actor 11, Actor 12', 'A royal adventure')

]

# Insert data into movies_movie table
for data in movies_movie_data:
    cursor.execute("""
        INSERT INTO movies_movie (id, name, image, rating, "cast", description)
        VALUES (%s, %s, %s, %s, %s, %s );
    """, data)

#Sample data for movies_seat table
movies_seat_data = [
    (1, 'A1', False, 1),
    (2, 'A2', True, 1),
    (3, 'B1', False, 1),
    (4, 'B2', True, 1),
    (5, 'C1', False, 1),
    (6, 'C2', False, 1),
    
    (7, 'A1', False, 2),
    (8, 'A2', True, 2),
    (9, 'B1', False, 2),
    (10, 'B2', True, 2),
    (11, 'C1', False, 2),
    (12, 'C2', False, 2),
    
    
    (13, 'A1', False, 3),
    (14, 'A2', True, 3),
    (15, 'B1', False, 3),
    (16, 'B2', True, 3),
    (17, 'C1', False, 3),
    (18, 'C2', False, 3),
    
    (19, 'A1', False, 4),
    (20, 'A2', True, 4),
    (21, 'B1', False, 4),
    (22, 'B2', True, 4),
    (23, 'C1', False, 4),
    (24, 'C2', False, 4),
    
     
    (25, 'A1', False, 5),
    (26, 'A2', True, 5),
    (27, 'B1', False, 5),
    (28, 'B2', True, 5),
    (29, 'C1', False, 5),
    (30, 'C2', False, 5),
    
    
      
    (31, 'A1', False, 6),
    (32, 'A2', True, 6),
    (33, 'B1', False, 6),
    (34, 'B2', True, 6),
    (35, 'C1', False, 6),
    (36, 'C2', False, 6),
    
]

#Insert data into movies_seat table
for data in movies_seat_data:
    cursor.execute("""
        INSERT INTO movies_seat (id, seat_number, is_booked, theater_id)
        VALUES (%s, %s, %s, %s);
    """, data)

#Sample data for movies_theater table
movies_theater_data = [
    (1, 'Theater One', '2024-12-27 10:00:00+00', 1),
    (2, 'Theater Two', '2024-12-27 11:00:00+00', 2),
    (3, 'Theater Three', '2024-12-27 12:00:00+00', 3),
    (4, 'Theater Four', '2024-12-27 13:00:00+00', 4),
    (5, 'Theater Five', '2024-12-27 14:00:00+00', 5),
     (6, 'Theater six', '2024-12-27 14:00:00+00', 6)
]

#Insert data into movies_theater table
for data in movies_theater_data:
    cursor.execute("""
        INSERT INTO movies_theater (id, name, time, movie_id )
        VALUES (%s, %s, %s, %s);
    """, data)

# Commit the transaction
# data = ("https://www.youtube.com/watch?v=Way9Dexny3w", 1)

cursor.execute("""
    UPDATE movies_seat
    SET is_booked = FALSE
    
""")





# cursor.execute("TRUNCATE TABLE auth_user CASCADE")
# cursor.execute("TRUNCATE TABLE movies_theater CASCADE")
# cursor.execute("TRUNCATE TABLE movies_seat CASCADE")
# cursor.execute("TRUNCATE TABLE movies_movie CASCADE")

conn.commit()

# Close cursor and connection
cursor.close()
conn.close()