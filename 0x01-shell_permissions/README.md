0-iam_betty: Switches the current user to the user Betty.
1-who_am_i: Prints the effective username of the current user.
2-groups: Prints all the groups the current user is part of.
3-new_owner: Changes the owner of the file hello to the user betty.
4-empty: Creates an empty file called hello.
5-execute: Creates a script that adds exeute permissions to the owner of the file hello.
6-multiple_permissions: Adds execute permission to the owner and the group owner, and read permission to oher users, to the file hello.
7-everybody: Adds execution permission to the owner, group owner and the other users to the file hello.
8-James_Bond: Sets the permission to the file hello as follows:
	Owner - no permission at all
	Group - no permission at all
	Other users - all the permissions
9-John_Doe: sets the mode of the file hello to this:
	-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
