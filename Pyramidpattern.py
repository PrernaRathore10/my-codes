# STAR PATTERN
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 



# Function to demonstrate printing pattern triangle
def triangle(n):

	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1

		for j in range(0, i+1):
			print("* ", end="")

		print("\r")


# Driver Code
n = 5
triangle(n)
