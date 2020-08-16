def main():
      time = input("Enter a number from 1 to 12: ")
      items = input("Enter a noun (plural):")
      name = input("Enter a name: ")
      scream = input("Enter any sentence:  ")
      verb = input("Enter a verb:")
      print ("It was" + time + " o'clock when I heard a knock at the door.I opened the door and there was a box full of "
      + items + " with a note saying \"From Mr. " + name.title()+"\
      Just as I closed the door I heard a scream \"" + scream.upper() + "\" I froze in place and all I could do " + verb +".")

if __name__ == '__main__':
	main()
