#list for rooms in the house
ROOMS = ['livingroom','gameroom','basement','attic','bathroom']

def read_motion(location_name):
    #list for detected rooms in motion check
    detected_rooms = []
    #opening the file
    f = open(location_name + ".motion.txt", "r")

    #checking for every line in the file
    for line in f:
        #creating a list for each detection
        detection = []
        #splitting each line at the comma to give the list
        detection.extend(line.split(",")) 
        #[0] is the room, [1] is the unneeded timestamp and [2] is whether it's detected or not
        #had trouble verifying the verdict without putting into another variable, so I put it into another variable and it detected properly after removing the newline
        verdict = detection[2].replace("\n", "")
        #checks if the room is detected
        if verdict == "detected":
            #if it is, it checks to see if it's already in the list or not
            if detection[0] not in detected_rooms:
                #if not, it gets added to the list and saved for later
                detected_rooms.append(detection[0])
        #resetting the list
        del(detection)
    
    #closing the file
    f.close()
    return(detected_rooms)

def read_emf(location_name):
    current_room = "UNKNOWN"
    current_sum = 0
    readings = 0
    room_readings = []
    #Opens the file
    with open(location_name + ".emf.txt", "r") as f:
        for line in f:
            if line.strip().isdigit():
                if current_room == "UNKNOWN":
                    print("Error reading EMF values")
                else:
                    #adds the amount to the current sum
                    current_sum += int(line)
                    #adds 1 to note of the readings
                    readings += 1
            else:
                if readings != 0:
                    #new room
                    if current_sum / readings > 3:
                        #adds to the list of rooms if the sum / readings is greater than 3
                        room_readings.append(str(current_room))
                    current_room = line.strip()
                    current_sum = 0
                    readings = 0
                else:
                    #first check
                    current_room = line.strip()
                    current_sum = 0
                    readings = 0
    f.close()
    return(room_readings)

def is_valid_temp(val):
    #sets the temp to a string
    temp = str(val)
    #strips the - away
    temp = temp.strip("-")
    #splits at .
    temp.split(".")
    #checks if the 1st input is an integer
    if temp[0].isdigit():
        return(True)
    else:
        return(False)

def read_temp(location_name):
    current_room = "UNKNOWN"
    consecutive = 0
    room_readings = []
    #opens the file
    with open(location_name + ".temp.txt", "r") as f:
        for line in f:
            if is_valid_temp(line.strip()) == True:
                if current_room == "UNKNOWN":
                    print("Error reading temperature values.")
                else:
                    #if the float is less than 0, it adds 1 to the consecutive
                    if float(line.strip()) < 0:
                        consecutive += 1
                        #if it's equal to or greater than 5, it'll check if the room is in the final list and if it's not, it'll add it and reset the consecutive
                        if consecutive >= 5:
                            if current_room not in room_readings:
                                room_readings.append(current_room)
                                consecutive = 0
                    else:
                        #if it's greater than or equal to 0, it'll reset the consecutive
                        consecutive = 0
            else:
                #changes room and resets consecutive
                current_room = line.strip()
                consecutive = 0
    f.close()
    return(room_readings)

def generate_report(location, motion, emf, temp):
    with open("ghost_report." + location + ".txt", "w") as f:
        f.write("------ [RGHS] Start of Haunting Report [RGHS] ------\n")
        f.write("Location: " + location.upper() + "\n")
        for i in ROOMS:
            if i in motion:
                if i in emf:
                    if i in temp:
                        f.write("There is a Poltergeist in the " + i.upper() + "\n")
                    else:
                        f.write("There is an Oni in the " + i.upper() + "\n")
                else:
                    if i in temp:
                        f.write("There is a Banshee in the " + i.upper() + "\n")
                    else:
                        f.write("There are no ghosts in the " + i.upper() + "\n")
            else:
                if i in emf:
                    if i in temp:
                        f.write("There is a Phantom in the " + i.upper() + "\n")
                    else:
                        f.write("There are no ghosts in the " + i.upper() + "\n")
                else:
                    if i in temp:
                        f.write("There are no ghosts in the " + i.upper() + "\n")
                    else:
                        f.write("There are no ghosts in the " + i.upper() + "\n")
        f.write("------- [RGHS] End of Haunting Report [RGHS] -------")

def main():
    print("[RGHS] Starting report: ")
    motion_detected_rooms = read_motion("house")
    emf_detected_rooms = read_emf("house")
    temp_detected_rooms = read_temp("house")
    print("[RGHS] Report finished, located in file: ghost_report.house.txt")
    generate_report("house", motion_detected_rooms, emf_detected_rooms, temp_detected_rooms)

if __name__ == "__main__":
    main()