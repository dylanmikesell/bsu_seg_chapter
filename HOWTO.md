
# How to get started

### Github

* Fork the master repository to your personal github account.

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
  $ clone https://github.com/[your-github-name]/bsu_seg_chapter.git
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
### Github again

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

* Push your committed work online,

  ```
  $ git push origin master
  ```