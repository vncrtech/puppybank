# Practice Test Automation Using a Local Web Application
For a long time, Selenium was the dominant player in the world of test automation. However, new contenders like Cypress and Playwright have emerged and gained popularity. More tools may arrive in the future. The important thing is that the need to upskill and practice will always be there. If you are here, you have already realized this.

To practice, we need a web application to play with. We can’t use public websites because we don’t have control over the changes they make. We need a controlled environment, a web application running on our local machine.

Introducing **Puppy Bank**.

**Puppy Bank** is an imaginary bank for puppies. It is a web application where puppies can process deposits, withdrawals, and transfers.

![Puppy Bank Tour](static\img\puppybank.gif)

Since you are looking for a web app to play with, I made it accessible for you and everyone.

## Have it run in two easy steps!

1. Download Docker Desktop. Wait for the installation to complete.
2. Run this command: ```docker run -d -p 8000:8000 vncrtech/puppybank```

That’s it. Puppy Bank is now accessible on your machine by going to ```http://localhost:8000```

The default credentials are admin/password.

**Note: Next time you want to bring up the application, there is no need to rerun the previous command, just go to Docker Desktop then Containers. Press the start button for Puppy Bank and it should be accessible again on localhost.*

You now have access to a web application specifically created for practicing test automation.

If you find this web application useful, you can show your support by clapping on this article on [Medium](https://vncrtech.medium.com/practice-test-automation-using-a-local-web-application-f8310ca37637) and sharing it with a friend. If you have a GitHub and/or Docker Hub account, you can also give a star to the repository. I would greatly appreciate it. Thank you!

**Docker:** https://hub.docker.com/r/vncrtech/puppybank

**Source Code:** https://github.com/vncrtech/puppybank

Enjoy learning new technologies and happy testing!
