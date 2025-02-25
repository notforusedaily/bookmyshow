{% extends "users/basic.html" %} {% block content %}
<div class="container mt-5">
  <div class="row">
    <div class="col-lg-10 mx-auto">
      <!-- Movie and Theater Info -->
      <div class="card mb-4">
        <div class="card-body">
          <div class="d-flex justify-content-between align-items-center flex-wrap">
            {% if messages %}
            <ul class="list-unstyled w-100">
                {% for message in messages %}
                    <li class="alert alert-{{ message.tags }} position-relative">
                        {{ message }}
                        <!-- Close button -->
                        <button class="close-btn" onclick="this.parentElement.style.display='none'">&times;</button>
                    </li>
                {% endfor %}
            </ul>
            {% endif %}
            
            <div>
              <h4 class="card-title">{{ theaters.movie.name }}</h4>
              <p class="card-text text-muted">
                {{ theaters.name }} | {{ theaters.time }}
              </p>
            </div>
            <div class="mt-2 mt-sm-0">
              <button class="btn btn-outline-primary me-2 mb-2 mb-sm-0">2D</button>
              <button class="btn btn-outline-primary me-2 mb-2 mb-sm-0">3D</button>
              <button class="btn btn-outline-primary mb-2 mb-sm-0">IMAX 3D</button>
              <button class="btn btn-outline-primary mb-2 mb-sm-0">
                {{seats|length}} Tickets
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Seat Selection -->
      <div class="card">
        <div class="card-body">
          <h5 class="card-title text-center mb-4">Select Your Seats</h5>
          
          <!-- Screen Area -->
          <div class="screen mb-5">SCREEN</div>

          <form method="POST">
            {% csrf_token %}
            
            <!-- Seat Layout - Fixed to display seats horizontally -->
            <div class="theater-container mb-5">
              {% with rows="ABCDEFGH"|make_list %}
                {% for row in rows %}
                  <div class="seat-row mb-3">
                    <div class="row-label">{{ row }}</div>
                    <div class="seats-in-row">
                      {% for seat in seats %}
                        {% if seat.seat_number.0 == row %}
                          <div class="seat {% if seat.is_booked %}sold{% endif %}" id="seat-container-{{ seat.id }}">
                            {% if not seat.is_booked %}
                              <input
                                type="checkbox"
                                name="seats"
                                value="{{ seat.id }}"
                                class="d-none"
                                id="seat-{{ seat.id }}"
                              />
                              <label
                                for="seat-{{ seat.id }}"
                                class="w-100 h-100 d-flex align-items-center justify-content-center"
                                >{{ seat.seat_number }}</label>
                            {% else %} 
                              {{ seat.seat_number }} 
                            {% endif %}
                          </div>
                          
                          <!-- Add aisle after every 5th seat -->
                          {% if seat.seat_number.1 == '5' %}
                            <div class="aisle"></div>
                          {% endif %}
                        {% endif %}
                      {% endfor %}
                    </div>
                  </div>
                {% endfor %}
              {% endwith %}
            </div>

            <!-- Seat Legend -->
            <div class="d-flex justify-content-center mb-4">
              <div class="d-flex align-items-center me-4">
                <div class="seat" style="background-color: white"></div>
                <span class="ms-2">Available</span>
              </div>
              <div class="d-flex align-items-center me-4">
                <div class="seat selected"></div>
                <span class="ms-2">Selected</span>
              </div>
              <div class="d-flex align-items-center">
                <div class="seat sold"></div>
                <span class="ms-2">Sold</span>
              </div>
            </div>

            <!-- Book Button -->
            <div class="text-center">
              <button type="submit" class="btn btn-success btn-lg">
                Book Selected Seats
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  body {
    font-family: Arial, sans-serif;
  }
  
  /* Theater and Screen Styling */
  .theater-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }
  
  .seat-row {
    display: flex;
    align-items: center;
    width: 100%;
    justify-content: center;
    margin-bottom: 10px;
  }
  
  .row-label {
    width: 30px;
    text-align: center;
    font-weight: bold;
    margin-right: 15px;
  }
  
  .seats-in-row {
    display: flex;
    flex-direction: row; /* Ensure horizontal layout */
    flex-wrap: nowrap; /* Prevent wrapping */
    gap: 8px;
    justify-content: center;
  }
  
  /* Aisle styling */
  .aisle {
    width: 25px;
    height: 35px;
    margin: 3px;
  }
  
  /* Screen styling */
  .screen {
    width: 80%;
    margin: 0 auto 30px;
    background: linear-gradient(to bottom, #555, #333);
    height: 40px;
    text-align: center;
    line-height: 40px;
    color: white;
    border-radius: 5px;
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    font-weight: bold;
    position: relative;
    overflow: hidden;
    transform: perspective(100px) rotateX(-5deg);
  }
  
  .screen:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: rgba(255, 255, 255, 0.3);
  }
  
  /* Seat styling */
  .seat {
    width: 35px;
    height: 35px;
    border: 1px solid #28a745;
    margin: 3px;
    text-align: center;
    line-height: 35px;
    cursor: pointer;
    border-radius: 5px 5px 10px 10px;
    transition: background-color 0.3s, color 0.3s;
    position: relative;
    overflow: hidden;
    background-color: #f8f9fa;
    font-size: 12px;
    flex-shrink: 0; /* Prevent seats from shrinking */
  }
  
  .seat:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: rgba(0, 0, 0, 0.1);
  }
  
  .seat:hover:not(.sold) {
    background-color: #28a745;
    color: white;
  }
  
  .seat.selected {
    background-color: #28a745;
    color: white;
  }
  
  .seat.sold {
    background-color: #e0e0e0;
    border-color: #bdbdbd;
    cursor: not-allowed;
    color: #999;
  }
  
  /* Checkbox styling */
  input[type="checkbox"]:checked + label {
    background-color: #4caf50;
    color: white;
    border-radius: 5px 5px 10px 10px;
  }
  
  /* Alert styling */
  .alert {
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 15px;
    position: relative;
  }
  
  .alert-success {
    color: #155724;
    background-color: #d4edda;
    border-color: #c3e6cb;
  }
  
  .alert-error, .alert-danger {
    color: #721c24;
    background-color: #f8d7da;
    border-color: #f5c6cb;
  }
  
  .alert-warning {
    color: #856404;
    background-color: #fff3cd;
    border-color: #ffeeba;
  }
  
  .alert-info {
    color: #0c5460;
    background-color: #d1ecf1;
    border-color: #bee5eb;
  }
  
  .close-btn {
    position: absolute;
    top: 5px;
    right: 10px;
    font-size: 16px;
    cursor: pointer;
    background: none;
    border: none;
  }
</style>

{% endblock %}

{% block scripts %}
<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Get all seat checkboxes
    const seatCheckboxes = document.querySelectorAll('input[name="seats"]');
    
    // Add click event listeners to the seat labels
    seatCheckboxes.forEach(checkbox => {
      const label = document.querySelector(`label[for="${checkbox.id}"]`);
      
      if (label) {
        label.addEventListener('click', function() {
          // Toggle the selected class on the parent seat div
          const seatDiv = this.parentElement;
          seatDiv.classList.toggle('selected');
        });
      }
    });
    
    // Theater ID for WebSocket connection
    const theaterId = {{ theaters.id }};
    
    // Connect to WebSocket
    try {
      const socket = new WebSocket(`ws://${window.location.host}/ws/seats/${theaterId}/`);
      
      socket.onopen = function() {
        console.log("Connected to WebSocket!");
      };
      
      socket.onmessage = function(event) {
        try {
          const data = JSON.parse(event.data);
          if (data.seats) {
            // Update seat availability in real-time
            data.seats.forEach(seat => {
              const seatContainer = document.getElementById(`seat-container-${seat.id}`);
              if (seatContainer) {
                if (seat.is_booked) {
                  // Mark seat as sold
                  seatContainer.classList.add('sold');
                  seatContainer.classList.remove('selected');
                  seatContainer.innerHTML = seat.seat_number;
                } else {
                  // Mark seat as available
                  seatContainer.classList.remove('sold');
                  if (seatContainer.querySelector('input') === null) {
                    seatContainer.innerHTML = `
                      <input type="checkbox" name="seats" value="${seat.id}" class="d-none" id="seat-${seat.id}" />
                      <label for="seat-${seat.id}" class="w-100 h-100 d-flex align-items-center justify-content-center">
                        ${seat.seat_number}
                      </label>
                    `;
                  }
                }
              }
            });
          }
        } catch (e) {
          console.error("Error processing WebSocket message:", e);
        }
      };
      
      socket.onerror = function(error) {
        console.error("WebSocket error:", error);
      };
    } catch (e) {
      console.error("Failed to establish WebSocket connection:", e);
    }
  });
</script>
{% endblock %}
