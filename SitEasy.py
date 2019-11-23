#SIT EASY APPLICATION IN PYTHON


def menu():
    #identation here
    #system("clear"); #alternate for python
	print("\n\n--------Menu-----------")
    print("\n1.Add a class ")
	print("\n2.Generate seating arrangement")
	print("\n3.Calculate seating arrangement Percentage")
	print("\n4.Save present generated seating arrangement")
    print("\n5.Retrieve previous versions")
	print("\n6.Credits and About")
	print("\n7.Enter data to Calculate")
	print("\n8.Exit")
	choice=int(input())
	switch={
		1: add();break;
		2: generate();break;
	    3: calc();break;
		4: save();break;
		5: retrieve();break;
		6: credits();break;
		7: data_save();break;
		8: exit(0);
		#default : printf("\n Worng user choice Please enter a correct choice\n");
	}.get(choice,"Invalid Choice")
	}while(choice!=8);


if __init__=='__main__':
    welcome()
    menu()
    #footer()
