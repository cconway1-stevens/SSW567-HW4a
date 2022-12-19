Write a description of what you thought about when you were designing the code.  What did *you* think was important to do to make it easy to test the program?  What are some of the challenges that you faced when testing this assignment?

# Test Badge 
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/cconway1-stevens/SSW567-HW4a/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/cconway1-stevens/SSW567-HW4a/tree/main)
Screenshot 2022-12-18 at 6.56.31 PM.png incase link is broke 
# Description
I designed my code with the goal of being able to write unit tests. To facilitate this, I used if and else statements. I also made the decision to use the GitHub user ID as a parameter in order to make it easier to test the program. This allowed me to insert different user IDs to see how it affected the output of the code. For example, I could test whether the program was correctly printing the repository names by inserting a user ID that did not exist on GitHub, which would cause the API request to fail. To test the commit counts, I inserted a user ID with a repository that had no commits, which triggered the error message I added to the code.

One of the main challenges I faced while working on this project was dealing with the GitHub API and its rate limits. I had to frequently stop and come back to the code because I was limited in the number of requests I could make in an hour. This was frustrating at first, but once I got the hang of it and everything was working correctly, it was easy to test the results.

Another challenge I encountered was figuring out how to correctly retrieve the commit count for each repository. Initially, I just printed the length of the JSON file, but this did not give me the correct number of commits. It took some time to find the correct command to use to get the correct commit count for each repository.

Once I was able to successfully run all of my test cases, I achieved my goal for this project.


