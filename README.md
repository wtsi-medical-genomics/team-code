##Contents
In the spirit of [don't repeat yourself](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself), this repository aims to collect together any code that will aid team members in the course of their work. This can be individual scripts that perform a common task or whole repositories. The objective is to have a central store where code can be contributed to, downloaded, and improved upon.

##Overview
This repository consists ot two parts:

1. **Standalone script files** These are single script files written in any language. These can be added directly to the team-code repository, that is, wtsi-medical-genomics will 'own' the code. You don't have to contribute code in this way, you can instead create a repository, add your script, and finally add it as a submodule.

2. **Submodules** These are essentially repositories within another repository. All submodules listed here will be 'owned' by other people/organizations - wtsi-medical-genomics is simply pointing at them. Why have them? They are used to incorporate other's code into your projects. [See here](http://git-scm.com/book/en/v2/Git-Tools-Submodules) for more information about submodules.

Contributing to this repository does not require submitting a pull-request by those who are members of wtsi-medical-genomics. That is, there is no oversight in terms of code-review.

##How to get code from the repository
There are few ways to do this, depending on your needs. If at any point you want to contribute to improve or add to the code, see the adding and contributing sections below.

####I only want one script file
In this case you can simply navigate to the file in GitHub, right click on the "Raw" button at the top right of the screen and save the file to your machine.

####I want one of the submodules to use as a standalone repository
Within GitHub, click on the submodule and you will be taken the repository. From here you can copy the address of the repo (look for the clone URL) and clone it on your machine:

```
git clone <github repository URL>
```

This will create a directory that contains the repository wherever you run this command.

####I want one of the submodules to incorporate into my own project repository
Within GitHub, click on the submodule you will be incorporating into your repository and copy the clone URL. Within a terminal window, navgiate to your project repository's working directory (call it project-dir) and run the following

```
project-dir$ git submodule add <github repository URL>
project-dir$ git submodule init
project-dir$ git submodule update
```

####I want the team-code repository
Within a terminal window change to a suitable directory (call it `paren-direc`) on your local machine where you would like the team-code repository to reside and enter

```
parent-direc$ git clone --recursive https://github.com/wtsi-medical-genomics/team-code
```

This will create a directory called team-code and the `--recursive` flag will populate all of the submodules.

##How to update local code

####I want to update a local single script file
If you only have a single local file (ie not the team-code repository) you will need to re-download the file via github. See section *I only want one script file* to do this.

####I want to update a local submodule
Within a terminal window change directory to the submodule directory (eg sub-mod) and enter

```
sub-mod$ git checkout master
sub-mod$ git pull origin master
```

####I want to update a local clone of team-code repository
Within a terminal window change directory to the team-code repository and enter

```
team-code$ git checkout master
team-code$ git pull origin master
```

##How to add code
*Note: It is assumed you are a member of the WTSI-medical-genomics organization. If not, see the section 'I am not not a member of your team...'.*

Whether you are adding a single script or a submodule, you will need to clone the repository. See section *I want the whole repository* above to do this.


####If you are adding a single script
In this case you may have a short script that doesn't need to be placed in a repository on it's own.

```
team-code $ git pull origin master
team-code$ cp <your file> .
team-code$ git add <your file>
team-code$ git commit "Adding <your file>"
team-code$ git push origin master
```

To help others find a relevent script, it would be helpful to include documentation at the beginning of your script including:

Brief description of what the script does

* Arguments
* Output
* Exceptions that are raised (if relevant)

See the [Google Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html?showone=Comments#Comments) for examples of good commenting practice



####Adding a repository

These can be larger code bases that you have written and currently reside on your github account or they can be other people's/organization's github repositories that you just want to add here to make other's aware of their existence. 

Now you can add your repository as a submodule and commit/push this addition:
```
team-code$ git submodule add <github repository URL>
team-code$ git commit -m "Adding submodule <repository name>"
team-code$ git push origin master
```

If you own the repository, be sure to include a README.md that lists:

* A description of what the repository does
* Any dependencies
* Any compilation / installation instructions

See the [GitHub's markdown basiscs](https://help.github.com/articles/markdown-basics/) for syntax help.


##I want to contribute/improve existing code in the repository
*Note: It is assumed you are a member of the WTSI-medical-genomics organization. If not, see the section 'I am not not a member of your team...'.*



Whether you are adding a single script or a submodule, you will need to clone the repository. See section *I want the whole repository* above to do this.

#####I want to improve a single script file
Before you start developing, make sure you are contributing to an up to date version of the file by pulling any changes onto your local machine:

```
team-code$ git pull origin master
```

Write your changes to the file and commit them to your local repository. You can cycle through this writing/local commiting as many times as you like until you are happy with the end result:

```
...write some code to file.xyz...
team-code$ git add file.xyz
team-code$ git commit -m "Added feature 1 to file.xyz"
...write some code to file.xyz...
team-code$ git commit -m "Added feature 2 to file.xyz"
```

When your development cycle is complete, it's time to upload to team-code on GitHub. First, fetch any changes made to the commit made since you started development:

```
team-code$ git fetch origin master
```

And now attempt to merge these commits (if any) to your local repository:

```
team-code$ git merge origin/master
```

Now finally push to the server:

```
team-code$ git push origin/master
```

####I want to contribute to a submodule
In this case you must contribute to the repository that the submodule links to. For example, if Calc6000 is a submodule of team-code but is owned by JohnSmith then you will contribute changes to https://github.com/JohnSmith/Calc6000. A general outline of this process is:

1. Fork https://github.com/JohnSmith/Calc6000.
2. Clone your own github version onto your machine
3. Commit changes to your fork
4. Submit a pull request to the original owner, JohnSmith
5. If approved by JohnSmith, your changes will be merged into https://github.com/JohnSmith/Calc6000.

See [the GitHub documenation of this process](https://help.github.com/articles/fork-a-repo/) for more detailed information.


####I am not not a member of your team but I would like to make some contributions
If you want to contribute to a single script (not a submodule) go ahead and fork the repository.
