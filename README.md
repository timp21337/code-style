### Code Style ###

##### Style Examples and tips #####
* Javascript Style Guide - [`javascript.js`](javascript.js)
* CSS Stye Guide - [`css.css`](css.css)
* Pylint Style guide - [`pylint_rc.py`](pylint_rc.py)

##### IDE Config Files #####





* IntelliJ13 codestyle settings - [`IntelliJIdea13/config/codestyles/we7.xml`](/IntelliJIdea13/config/codestyles/we7.xml)
 * Place in `~/.IntelliJIdea13/config/codestyles/we7.xml` and 
   select from **Project Settings** - **Code Style** - **Scheme**


* JSHint Settings file - [`JSHint/.jshintrc`](/config/.jshintrc)
 * Edit the file to add your common globals
 * Place in project root, and in **Project Settings** - **JavaScript** - **Code Quality Tools** - **JSHint** enable **Use config files** and Version **2.1.3**

## Pylint ##

Pylint enables us to report conformance to our Python coding standard.
All projects, across all teams use the same pylint configuration file. 

Our standard is based up http://www.python.org/dev/peps/pep-0008/ and 
http://www.python.org/dev/peps/pep-0257/ however we disable some rules 
to ensure that the number of violations is readable. 

It is believed that the number of violations will fall natually when the 
IntelliJ/Idea python plugin gains built-in PEP-8 support. 



