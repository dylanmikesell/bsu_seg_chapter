
# How to get started

### Github (get exsiting work)

* Fork the master repository to your personal github account. You can do this by clicking the button *Fork* in the Master repo website.

	Master repository: 

  ```
  https://github.com/dylanmikesell/bsu_seg_chapter
  ```

* Make a directory where you want to work and go to it, for example:

  ```
  $ mkdir seg-bsu
  $ cd seg-bsu
  ```
* Clone your own fork to your personal computer:

  ```
  $ git clone https://github.com/[your-github-name]/bsu_seg_chapter.git
  ```

### Python

* Make sure you have Python 3.7. You can update by,

  ```
  $ conda update --all
  ```

* Go to the Anaconda app and follow,
	* click on 'Environments',
	* click on 'Create',
	* choose Python 3.7 and a name.
* Command line version:

	```
	$ conda create -n [name] python=3.7 anaconda
	```

### Write some code

* Go back to your working folder, for example:

  ```
  $ cd seg-bsu/bsu_seg_chapter/[specific package]/
  $ source activate [name of environment]
  $ jupyter notebook [name of notebook]
  ```
* Write stuff in the notebook.
* You can use/write python classes and functions in 

	```
	seg-bsu/bsu_seg_chapter/src/
	```

* To leave this python environment from your terminal,

  ```
  $ source deactivate
  ```
* All your work is saved in:

  ```
  seg-bsu/bsu_seg_chapter/[specific package]/[name of notebook]
  ```

### Github (add work - to your branch)

* Go back to

	```
  seg-bsu/bsu_seg_chapter/
  ```
  
* Add your work

	```
  $ git add .
  ```

* Commit your work with a message of what you did

  ```
  $ git commit -m "message"
  ```

* Push your committed work online

  ```
  $ git push origin master
  ```
  
### Github (merge with master)

* Go to your Github repo webpage

```
  https://github.com/[your-github-name]/bsu_seg_chapter
```

* Click *New pull request*
* Engage in a chat with the master
  
### Stay up to date with master branch  


* Add remote from original repository in your forked repository

	```
    $ cd seg-bsu/bsu_seg_chapter/
    $ git remote add upstream git://github.com/dylanmikesell/bsu_seg_chapter.git
   ``` 

* Updating your fork from original repo to keep up with their changes:

	```
	$ git fetch upstream
    $ git pull upstream master
   ```