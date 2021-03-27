import time
import random

COLOURS = ["red", "blue", "green", "yellow", "brown", "pink", "orange"]

def load_map(file_path):
    valid_paths = dict()
    valid_rooms = []
    with open(file_path, "r") as f:
        for line in f:
            split = line.strip().split(": ")
            for i in range(len(split)):
                valid_paths.update({split[0]:split[i]})
                if split[0] not in valid_rooms:
                    valid_rooms.append(split[0])
    f.close()
    return(valid_paths, valid_rooms)

def simplify_testimony(chat, rooms): #reminder: no location = useless, location no color = talking about self, location with color = claiming another crewmate in loc
    chat = chat.replace(".", "")
    chat = chat.replace(", ", " ")
    chat = chat.replace("?", "")
    premessage = chat.split(": ")
    if "voted" in premessage[0]:
        return(premessage[0])
    else:
        color_in_message = ""
        room_in_message = ""
        speaker = premessage[0]
        message = premessage[1].split(" ")
        for i in message:
            if i in COLOURS:
                color_in_message = i
            if i in rooms:
                room_in_message = i
        if room_in_message != "":
            if color_in_message != "":
                return(speaker + ": " + color_in_message + " in " + room_in_message)
            else:
                return(speaker + ": " + speaker + " in " + room_in_message)
        else:
            return(" ")


def load_chat_log(filename, rooms):
    message = []
    with open(filename, "r") as f:
        for line in f:
            message.append(simplify_testimony(line.strip(), rooms))
    return(message)
    f.close()

def tally_votes(chat_log):
    votes = dict()
    for c in COLOURS:
        votes.update({c:0})
    votes.update({"skip":0})
    for i in chat_log:
        if "voted" in i:
            votees = i.split(" voted ")
            votes[votees[1]] += 1
            votes.update({votees[1]:votes[votees[1]]})
    return(votes)

def get_paths(chat_log):
    paths = dict()
    locations = []
    current_color = "UNKNOWN"
    for c in COLOURS:
        paths.update({c:""})
    for i in chat_log:
        if i != " ":
            if "voted" not in i:
                message = i.split(": ")
                if message[0] in message[1]:
                    if message[0] != current_color:
                        if len(locations) > 0:
                            paths.update({current_color:locations})
                        current_color = message[0]
                        locations = []
                    location = message[1].split(" in ")
                    locations.append(location[1])
    paths.update({current_color:locations})
    return(paths)

def get_sus_paths(path_dict, rooms): #crewmate paths and valid paths
    current_location = "UNKNOWN"
    old_location = "UNKNOWN"
    current_color = "UNKNOWN"
    suspicious = []
    for i in path_dict:
        for d in path_dict[i]:
            if i != current_color:
                current_color = i
                current_location = d
            else:
                new_location = d
                if current_location not in rooms[new_location]:
                    suspicious.append(current_color)
                current_location = d
    return(suspicious)

def main():
    print("----------- Loading Map. -----------")
    valid_paths, valid_rooms = load_map("skeld.txt")
    print("----------- Map Loaded. -----------")
    #t = random.uniform(1, 5) #Waiting a specific amount of seconds before meeting called and everyone chats. Remove the pound signs if you wish to have the delay.
    #time.sleep(t)
    print("------------- Meeting Called! -------------")
    messages = load_chat_log("chatlog.txt", valid_rooms)
    for i in messages:
        if i != " ":
            #time.sleep(0.5)
            print(i)
    print("------------- Meeting Ended! -------------")
    #time.sleep(1)
    print("------------- Tallying Votes! -------------")
    #time.sleep(1)
    votes = tally_votes(messages)
    for i in votes:
        print(i + ": " + str(votes[i]))
    #time.sleep(1)
    print("------------- Votes Tallied! -------------")
    paths = get_paths(messages)
    suspicious = get_sus_paths(paths, valid_paths)
    #time.sleep(1)
    print("------------- Liars! -------------")
    print(suspicious)


if __name__ == "__main__":
    main()