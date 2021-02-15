import os
import shutil
import time

def main():
	folders_deleted = 0
	files_deleted = 0
  
	days = 30

	path = input('Enter the path to organize and delete: ')

	seconds = time.time() - (days*24*60*60)


	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= get_file_or_folder_age(root_folder):
				remove_folder(root_folder)
				folders_deleted = folders_deleted + 1
				break

			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= get_file_or_folder_age(folder_path):
						remove_folder(folder_path)
						folders_deleted = folders_deleted + 1


				for file in files:
					file_path = os.path.join(root_folder, file)
						if seconds >= get_file_or_folder_age(file_path):
							remove_file(file_path)
							files_deleted = files_deleted + 1

			else:
				if seconds >= get_file_or_folder_age(path):
					remove_file(path)
					files_deleted = files_deleted + 1

	else:
		print(path, 'is not found')
		files_deleted = files_deleted + 1

	print('Total folders deleted:', folders_deleted)
	print('Total files deleted:', files_deleted)


def remove_folder(path):
	if not shutil.rmtree(path):
		print(path, 'is removed successfully')

	else:
		print('Unable to delete the', path)



def remove_file(path):
	if not os.remove(path):
		print(path, 'is removed successfully')

	else:
		print('Unable to delete the', path)


def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime

	return ctime

if __name__ == '__main__':
	main()