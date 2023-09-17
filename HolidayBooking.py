#Daniel O'Driscoll
#R00221504

#sorry in advance for the messy code, i rushed to finish some parts towards the end but ill try comment below to make it clearer :)



def menu():											#menu function with loop ensuring correct input
	valid_num = (1, 2, 3)
	i = 0
	print("\nLONG ISLAND HOLIDAYS")
	print("="*20)
	print("1. Make a booking")
	print("2. Review bookings")
	print("3. Exit")
	while i == 0:								
		user_choice = int(input("\n=> "))
		if user_choice in valid_num:
			return user_choice



def kids_pool_record(num_kids, num_passes):									#function that increments pool/kids in extras.txt

	with open("Extras.txt", 'r') as my_extras_file:
		line_number = my_extras_file.readlines()							#'r' so i can use readline(),
		split_kids_line = line_number[0].split(',')							#split lines into list
		split_pool_line = line_number[1].split(',')	

		if num_kids == 0 and num_passes == 'Z':
			split_kids_line[1] = int(split_kids_line[1])				#kids=0, num_passes='z' ensures my review function later
			split_pool_line[1] =  int(split_pool_line[1])				#making numbers in extras.txt unchanged (when user doesnt make booking they wont increment)

		else:
			if num_kids > 0:
				split_kids_line[1] = int(split_kids_line[1]) + num_kids		#else (when user makes the booking) increment the numbers on extras.txt
			if num_passes[0].upper() == 'Y':
				split_pool_line[1] =  int(split_pool_line[1]) + 1



	with open("Extras.txt", 'w') as my_extras_file:
		print(f"kids camp, {split_kids_line[1]}", file=my_extras_file)		#overwrite the file with same format but with updated or unchanged numbers
		print(f"pool pass, {split_pool_line[1]}", file=my_extras_file)

	return split_kids_line[1], int(split_pool_line[1])						#return total kids, total pool passes from extra.txt





def reading_file(textfile):													#function that takes in bookings2022.txt and returns
	accomodation_lst = []													#list of acommodation types, costs, current bookings
	prices_lst = []
	bookings_lst =[]
	with open(textfile) as my_textfile:
		for line in my_textfile:
			split_line = line.split(',')
			accomodation_lst.append(split_line[0])
			prices_lst.append(int(split_line[1]))					
			bookings_lst.append(int(split_line[2]))
		return accomodation_lst, prices_lst, bookings_lst



def updateBookings2022(accom_type):
	info_from_textfile = reading_file("Bookings_2022.txt")							#function updates bookings2022.txt numbers
	lst_of_current_bookings = info_from_textfile[2]									#calls result of readingfile()
																					#assigning the current bookings list at index 2 from the result above to a variable
	if accom_type == 1:
		lst_of_current_bookings[0] = int(lst_of_current_bookings[0]) + 1			#find accomodation they chose 1,2 or 3 through accom_type parameter
	elif accom_type == 2:															#e.g lst_of_current_bookings[1] would be bookings for standard caravan from the list above
		lst_of_current_bookings[1] = int(lst_of_current_bookings[1]) + 1
	elif accom_type == 3:
		lst_of_current_bookings[2] = int(lst_of_current_bookings[2]) + 1


	with open('Bookings_2022.txt', 'w') as myBookingFile:
			print(f"Deluxe Caravan,2000,{lst_of_current_bookings[0]}", file=myBookingFile)			#overwite file with same format, updated numbers
			print(f"Standard Caravan,1600,{lst_of_current_bookings[1]}", file=myBookingFile)
			print(f"Camp,200,{lst_of_current_bookings[2]}", file=myBookingFile)

	return lst_of_current_bookings[0], lst_of_current_bookings[1], lst_of_current_bookings[2]		#return updated numbers of bookings.txt for the review function later



def BookingReview(accom_lst, total_pool_kids ,current_id):											#review function
	most_popular = max(accom_lst)																	#max value from the returned results in previous function
	expected_income = accom_lst[0] * 2000 + accom_lst[1] * 1600 + accom_lst[2] * 200 + total_pool_kids[1] * 150 + total_pool_kids[0] *100 	#multiply each booking amount by appropriate cost
	average = expected_income / current_id				#average is the total expected divided by the number of booking so far
	remaining_sites = 30 - current_id					#bookings left is total allowed bookings minus the current 

	print(f"\nLONG ISLAND HOLIDAYS = Review Bookings")
	print("="*20)
	print(f"Deluxe Caravan: {accom_lst[0]}")
	print(f"Standard Caravan: {accom_lst[1]}")
	print(f"Camp Site: {accom_lst[2]}")
	print(f"Total no. of pool passes: {total_pool_kids[1]}")			#print out review table
	print(f"No. for Kids Club: {total_pool_kids[0]}")
	print(f"Most popular accomodation: {most_popular}")
	print(f"Expected Income: €{expected_income}")
	print(f"Average per booking: €{average}")
	print(f"Number of remaining sites: {remaining_sites}")


def make_booking():																		#make booking function
	KIDS_CLUB, FAMILY_PASS = 100, 150
	accomodation_option = (0, 2000, 1600, 200, 0)										#tuple/constant/lsts for easier user further down
	accomodation_lst = ['BLANK', 'Deluxe Caravan', 'Standard Caravan', 'Camp Site']

	info_from_textfile = reading_file("Bookings_2022.txt")						#get current bookings from booking.txt again to show it in the table further down
	lst_of_current_bookings = info_from_textfile[2]

																	
	surname = input("Please enter your surname: ")
	while (len(surname) > 14 or len(surname) < 1) or surname.isalpha() == False:			#asking for info with error checks
		surname = input("Please enter your surname: ")
																				
	phone = input("Please enter your phone number: ")
	while len(phone) >= 12 or phone.isnumeric() == False:
		phone = input("Please enter your phone number: ")

	print("Choose your accomodation type: ")					
	print(f"1. Deluxe Caravan (€2000.0) {lst_of_current_bookings[0]} booked")
	print(f"2. Standard Caravan (€1600.0) {lst_of_current_bookings[1]} booked")		#displaying currnet bookings from calling readingfile()
	print(f"3. Camp site (€200.0) {lst_of_current_bookings[2]} booked")
	print("4. No Booking")

	accomodation_type = int(input("=> "))
	while accomodation_type < 1 or accomodation_type > 4 or str(accomodation_type).isnumeric() == False:
		accomodation_type = int(input("Choose your accomodation type: "))

	if accomodation_type == 4:																#if 4 skip rest of the info and returns to menu whilst retuning value 4
		return 4
		

	else:
		group_amount = int(input("Please enter the amount of people attending: "))			#if not 4, enter more info with error checks		
		while group_amount <= 0 or str(group_amount).isnumeric() == False:
			group_amount = int(input("Please enter the amount of people attending: "))

		kids_amount = int(input("Please enter the amount of kids attending kids club:  "))
		while kids_amount >= group_amount:
			kids_amount = int(input("Please enter the amount of kids attending kids club:  "))


		pool_pass = input("Would you like to purchase a pool pass (Y/N)? ")
		while pool_pass[0].upper() != 'Y' and pool_pass[0].upper() != 'N':
			pool_pass = input("Would you like to purchase a pool pass (Y/N)? ")

		total_cost = accomodation_option[accomodation_type] + (kids_amount * KIDS_CLUB)					#get total
		
		if pool_pass.upper() == 'Y':
			pool_pass = 'Yes'
			total_cost = total_cost + FAMILY_PASS												#added family pass cost only if yes
		else:
			pool_pass = 'No' 											#accomodation_lst[accomodation_type] returns the name of the selected accomodation

		return surname, phone, group_amount, kids_amount, pool_pass, accomodation_lst[accomodation_type], total_cost, accomodation_type


def receipt(username, accom, group, pool, kids, total, accom_num, booking_id):		#prints receipt to the screen
	accomodation_option = (0, 2000, 1600, 200)

	print("\nBooking Details")												
	print("-"*20)
	print(f"Name: {username}")
	if booking_id < 10:
		print(f"Booking id: 0{booking_id}")
	else:
		print(f"Booking id: {booking_id}")							#takes varaibels needed for a receipt

	print(f"Accomodation type: {accom}")
	print(f"No. of people: {group}")
	print(f"Pool Pass: {pool}")
	print(f"No. for kids club: {kids}")
	print(f"Accomodation Cost: €{accomodation_option[accom_num]}")
	print(f"Cost: €{total}\n")


	if booking_id < 31:
		if booking_id < 10:													#enures only 30 bookings can be made
			booking_id = "0" + str(booking_id)								#prints id 01, 02....

		with open(f"{username.capitalize()}_{booking_id}.txt", 'w') as familyReceipt:
			print("\nBooking Details", file=familyReceipt)												
			print("-"*20, file=familyReceipt)
			print(f"Name: {username}", file=familyReceipt)											#prints same receipt but in file with users name and id
			print(f"Booking id: {booking_id}", file=familyReceipt)
			print(f"Accomodation type: {accom}", file=familyReceipt)
			print(f"No. of people: {group}", file=familyReceipt)
			print(f"Pool Pass: {pool}", file=familyReceipt)
			print(f"No. for kids club: {kids}", file=familyReceipt)
			print(f"Accomodation Cost: €{accomodation_option[accom_num]}", file=familyReceipt)
			print(f"Cost: €{total}", file=familyReceipt)



def main():
	menu_selection = 0
	current_id = 0								#initialize menu loop and id incremntation for booking

	while menu_selection != 3:
		menu_selection = menu()						#calls menu function
		current_id = current_id + 1					# assigns booking id to 1

		if menu_selection == 1:			
			user_booking = make_booking()			#if 1 (make booking) got to booking function

			if user_booking == 4:					#if 4 (no booking from make_booking()) skip rest of booking and updating phase with continue statement
				continue

			else:											#makes booking
				num_kids = user_booking[3]					#assigning returned values from make_booking() to variables
				pool_pass = user_booking[4]
				user_name = user_booking[0]
				user_groupNum = user_booking[2]
				user_acommodation_name = user_booking[5]
				user_acommodation_num = user_booking[7]
				user_cost = user_booking[6]

				iterate_extras = kids_pool_record(num_kids, pool_pass)			#update kids and pool in extra.txt
				updated_bookings = updateBookings2022(user_acommodation_num)	#update bookings.txt
				user_receipt = receipt(user_name, user_acommodation_name, user_groupNum, pool_pass, num_kids, user_cost, user_acommodation_num, current_id)		#get receipt
				
																		
		elif menu_selection == 2:
			#call reviews of bookings
			BookingReview(updated_bookings, kids_pool_record(0, 'Z'), current_id)		#review function with kids_pool_record(0, 'Z') to show current kids and pool 
																						#and avoid updating them, current id for user, and current bookings in the argument
		elif menu_selection == 3:
			exit()															#user inputs 3 quit loop

		elif current_id == 31:												#over 30 bookings quit loop
			exit()
											



if __name__ == '__main__':
	main()