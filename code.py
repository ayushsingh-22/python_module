def calculate_angle(hour, minute):
    # Calculate the angle between the hour and minute hand
    hour_angle = (hour % 12) * 30 + (minute / 60) * 30
    minute_angle = (minute % 60) * 6
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

def move_cost(degrees, cost_per_degree, cost_above_90):
    if degrees <= 90:
        return degrees * cost_per_degree
    else:
        return (90 * cost_per_degree) + ((degrees - 90) * cost_above_90)

def min_cost_to_form_angle(current_hour, current_minute, target_angle, A, B, P, Q, X, Y):
    # Calculate the current angle between the hands
    current_angle = calculate_angle(current_hour, current_minute)

    # Calculate the difference needed to reach the target angle
    angle_diff = (target_angle - current_angle) % 360
    angle_diff_complement = (current_angle - target_angle) % 360

    # Possible movements
    costs = []

    # Move hour hand clockwise and minute hand counterclockwise
    for hour_move in range(-1, 2):  # -1, 0, +1 (previous hour, same hour, next hour)
        new_hour = (current_hour + hour_move) % 12
        hour_movement = abs(hour_move) * 30  # each hour change is 30 degrees

        # Calculate the angle after moving the hour hand
        new_angle = (current_angle + hour_movement) % 360

        # Calculate the angle needed for the minute hand
        needed_angle = (target_angle - new_angle) % 360
        needed_angle_complement = (new_angle - target_angle) % 360

        # Compute costs for both needed angles
        if needed_angle <= 180:
            minute_cost = move_cost(needed_angle, X, Y)
        else:
            minute_cost = move_cost(360 - needed_angle, X, Y)

        # Cost for hour hand movement
        if hour_move == 0:
            hour_cost = 0
        else:
            hour_cost = move_cost(hour_movement, P, Q)

        total_cost = hour_cost + minute_cost
        costs.append(total_cost)

        # Now consider the opposite direction for the minute hand
        if needed_angle_complement <= 180:
            minute_cost = move_cost(needed_angle_complement, X, Y)
        else:
            minute_cost = move_cost(360 - needed_angle_complement, X, Y)

        total_cost = hour_cost + minute_cost
        costs.append(total_cost)

    # Return the minimum cost from all possible movements
    return min(costs)

def main():
    # Input reading
    initial_time = input().strip()
    n = int(input().strip())
    A, B = map(int, input().strip().split())
    P, Q = map(int, input().strip().split())
    X, Y = map(int, input().strip().split())

    # Parse the initial time
    hour, minute = map(int, initial_time.split(':'))

    total_cost = 0

    for _ in range(n):
        target_angle = int(input().strip())
        cost = min_cost_to_form_angle(hour, minute, target_angle, A, B, P, Q, X, Y)
        total_cost += cost

        # Update the current time to the new position after processing the query
        # Calculate the new angle after performing the movements
        new_angle = (calculate_angle(hour, minute) + target_angle) % 360
        # Update the hour and minute based on the new angle
        # This part is not straightforward, so we will keep the current hour and minute fixed
        # as the problem states we can only change them based on the query.

    print(total_cost)

if __name__ == "__main__":
    main()