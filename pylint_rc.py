[MASTER]

# Specify a configuration file.
#rcfile=

# Python code to execute, usually for sys.path manipulation such as
# pygtk.require().
#init-hook=

# Profiled execution.
profile=no

# Add files or directories to the blacklist. They should be base names, not
# paths.
ignore=CVS

# Pickle collected data for later comparisons.
persistent=yes

# List of plugins (as comma separated values of python modules names) to load,
# usually to register additional checkers.
load-plugins=


[MESSAGES CONTROL]

# Enable the message, report, category or checker with the given id(s). You can
# either give multiple identifier separated by comma (,) or put this option
# multiple time.
#enable=

# Disable the message, report, category or checker with the given id(s). You
# can either give multiple identifier separated by comma (,) or put this option
# multiple time (only on the command line, not in the configuration file where
# it should appear only once).

# By general agreement we do not need these
# C0301 Line too long
# C0103 Invalid name
# C0111 Missing docstring
# R0201 Method could be a function 
#         Used when a method doesn’t use its bound instance, 
#         and so could be written as a function.
# I0011 Warning locally suppressed using disable-msg


# W0704 Except doesn't do anything 
#         Used when an except clause does nothing but "pass" and there is no "else" clause
# W0142 Used * or * magic* 
#         Used when a function or method is called using *args or **kwargs to dispatch arguments.
# W0232 Class has no __init__ method 
#         Used when a class has no __init__ method, neither its parent classes.
# W0702 No exception's type specified 
#         Used when an except clause doesn't specify exceptions type to catch.
# E1101 %s %r has no %r member 
#         Used when a variable is accessed for an unexistent member.

# R0921 Abstract class not referenced 
#         Used when an abstract class is not used as ancestor anywhere.
# R0922 Abstract class is only referenced %s times 
#         Used when an abstract class is used less than X times as ancestor.
#         Is raised when abstract classes are used in different module
# E1103 %s %r has no %r member (but some types could not be inferred) 
#         Used when a variable is accessed for an unexistent member, 
#         but astng was not able to interpret all possible types of this variable.
# W0511 Used when a warning note as FIXME or XXX is detected.
# W0703 Catching too general exception Exception
# R0912 Too many branches (%s/%s) 
#         Used when a function or method has too many branches, making it hard to follow.
# R0913 Too many arguments (%s/%s) 
#         Used when a function or method takes too many arguments.
# W0613 Unused argument %r 
#        Used when a function or method argument is not used.
# R0801 Similar lines in %s files 
#         Indicates that a set of similar lines has been detected 
#         among multiple file. 
# W0232 Class has no __init__ method 
#         Used when a class has no __init__ method, neither its parent classes.
# R0903 Too few public methods (%s/%s) 
#         Used when class has too few public methods, so be sure it’s really worth it.
# W0603 Using the global statement 
#         Used when you use the “global” statement to update a global variable. 
# R0902 Too many instance attributes (%s/%s) 
#         Used when class has too many instance attributes
# W0223 Method %r is abstract in class %r but is not overridden 
#         Used when an abstract method (i.e. raise NotImplementedError) is not overridden in concrete class.
# W0212 Access to a protected member %s of a client class 
#         Used when a protected member (i.e. class member with a name beginning with an underscore) 
#         is access outside the class or a descendant of the class where it’s defined.

# R0911 Too many return statements (%s/%s) 
#         Used when a function or method has too many return statement, making it hard to follow.
# R0915 Too many statements (%s/%s) 
#         Used when a function or method has too many statements. You should then split it in smaller functions / methods.
# R0914 Too many local variables (%s/%s) 
#         Used when a function or method has too many local variables.
# E1305 Too many arguments for format string 
#         Used when a format string that uses unnamed conversion specifiers is given too few arguments.
# R0904 Too many public methods (%s/%s) 
#         Used when class has too many public methods, try to reduce this to get a more simple (and so easier to use) class.

# W0141 Used builtin function %r 
#         Used when a black listed builtin function is used (see the bad-function option). 
#         Usual black listed functions are the ones like map, or filter , where Python offers now some cleaner alternative like list comprehension.
# W0102 Dangerous default value %s as argument 
#         Used when a mutable value as list or dictionary is detected in a default value for an argument.

# Checks new with pylint 1.0
# C1001  Old-style-class
#        for classes that do not have any base class.
# C0304  Final newline missing
# C0303  Trailing whitespace
# W1201  Specify string format arguments as logging function parameters
# W1401  Anomalous backslash in string
# R0924  Badly implemented Contaner

# Agreed acceptable
#disable=C0301,C0103,C0111,R0201

# Currently required
disable=C0301,C0103,C0111,R0201,E1103,I0011,W0511,W0703,R0912,R0913,W0613,R0801,W0232,R0903,W0603,R0902,W0223,W0212,R0911,R0915,R0914,E1305,R0904,W0141,W0102,W1201

# Only available in the most recent version of pylint 
#C1001
#C0303
#C0304
#W1401
#R0924

[REPORTS]

# Set the output format. Available formats are text, parseable, colorized, msvs
# (visual studio) and html
output-format=text

# Include message's id in output
include-ids=no

# Put messages in a separate file for each module / package specified on the
# command line instead of printing them on stdout. Reports (if any) will be
# written in a file name "pylint_global.[txt|html]".
files-output=no

# Tells whether to display a full report or only the messages
reports=yes

# Python expression which should return a note less than 10 (10 is the highest
# note). You have access to the variables errors warning, statement which
# respectively contain the number of errors / warnings messages and the total
# number of statements analyzed. This is used by the global evaluation report
# (RP0004).
evaluation=10.0 - ((float(5 * error + warning + refactor + convention) / statement) * 10)

# Add a comment according to your evaluation note. This is used by the global
# evaluation report (RP0004).
comment=no


[VARIABLES]

# Tells whether we should check for unused import in __init__ files.
init-import=no

# A regular expression matching the beginning of the name of dummy variables
# (i.e. not used).
dummy-variables-rgx=_|dummy

# List of additional names supposed to be defined in builtins. Remember that
# you should avoid to define new builtins when possible.
additional-builtins=


[TYPECHECK]

# Tells whether missing members accessed in mixin class should be ignored. A
# mixin class is detected if its name ends with "mixin" (case insensitive).
ignore-mixin-members=yes

# List of classes names for which member attributes should not be checked
# (useful for classes with attributes dynamically set).
ignored-classes=SQLObject

# When zope mode is activated, add a predefined set of Zope acquired attributes
# to generated-members.
zope=no

# List of members which are set dynamically and missed by pylint inference
# system, and so shouldn't trigger E0201 when accessed. Python regular
# expressions are accepted.
generated-members=REQUEST,acl_users,aq_parent


[SIMILARITIES]

# Minimum lines number of a similarity.
min-similarity-lines=4

# Ignore comments when computing similarities.
ignore-comments=yes

# Ignore docstrings when computing similarities.
ignore-docstrings=yes


[FORMAT]

# Maximum number of characters on a single line.
max-line-length=80

# Maximum number of lines in a module
max-module-lines=1000

# String used as indentation unit. This is usually " " (4 spaces) or "\t" (1
# tab).
indent-string='    '


[BASIC]

# Required attributes for module, separated by a comma
required-attributes=

# List of builtins function names that should not be used, separated by a comma
bad-functions=map,filter,apply,input

# Regular expression which should only match correct module names
module-rgx=(([a-z_][a-z0-9_]*)|([A-Z][a-zA-Z0-9]+))$

# Regular expression which should only match correct module level names
const-rgx=(([A-Z_][A-Z0-9_]*)|(__.*__))$

# Regular expression which should only match correct class names
class-rgx=[A-Z_][a-zA-Z0-9]+$

# Regular expression which should only match correct function names
function-rgx=[a-z_][a-z0-9_]{2,30}$

# Regular expression which should only match correct method names
method-rgx=[a-z_][a-z0-9_]{2,30}$

# Regular expression which should only match correct instance attribute names
attr-rgx=[a-z_][a-z0-9_]{2,30}$

# Regular expression which should only match correct argument names
argument-rgx=[a-z_][a-z0-9_]{2,30}$

# Regular expression which should only match correct variable names
variable-rgx=[a-z_][a-z0-9_]{2,30}$

# Regular expression which should only match correct list comprehension /
# generator expression variable names
inlinevar-rgx=[A-Za-z_][A-Za-z0-9_]*$

# Good variable names which should always be accepted, separated by a comma
good-names=i,j,k,ex,Run,_

# Bad variable names which should always be refused, separated by a comma
bad-names=foo,bar,baz,toto,tutu,tata

# Regular expression which should only match functions or classes name which do
# not require a docstring
no-docstring-rgx=__.*__


[MISCELLANEOUS]

# List of note tags to take in consideration, separated by a comma.
notes=FIXME,XXX,TODO


[DESIGN]

# Maximum number of arguments for function / method
max-args=5

# Argument names that match this expression will be ignored. Default to name
# with leading underscore
ignored-argument-names=_.*

# Maximum number of locals for function / method body
max-locals=15

# Maximum number of return / yield for function / method body
max-returns=6

# Maximum number of branch for function / method body
max-branchs=12

# Maximum number of statements in function / method body
max-statements=50

# Maximum number of parents for a class (see R0901).
max-parents=7

# Maximum number of attributes for a class (see R0902).
max-attributes=7

# Minimum number of public methods for a class (see R0903).
min-public-methods=2

# Maximum number of public methods for a class (see R0904).
max-public-methods=20


[IMPORTS]

# Deprecated modules which should not be used, separated by a comma
deprecated-modules=regsub,string,TERMIOS,Bastion,rexec

# Create a graph of every (i.e. internal and external) dependencies in the
# given file (report RP0402 must not be disabled)
import-graph=

# Create a graph of external dependencies in the given file (report RP0402 must
# not be disabled)
ext-import-graph=

# Create a graph of internal dependencies in the given file (report RP0402 must
# not be disabled)
int-import-graph=


[CLASSES]

# List of interface methods to ignore, separated by a comma. This is used for
# instance to not check methods defines in Zope's Interface base class.
ignore-iface-methods=isImplementedBy,deferred,extends,names,namesAndDescriptions,queryDescriptionFor,getBases,getDescriptionFor,getDoc,getName,getTaggedValue,getTaggedValueTags,isEqualOrExtendedBy,setTaggedValue,isImplementedByInstancesOf,adaptWith,is_implemented_by

# List of method names used to declare (i.e. assign) instance attributes.
defining-attr-methods=__init__,__new__,setUp

# List of valid names for the first argument in a class method.
valid-classmethod-first-arg=cls


[EXCEPTIONS]

# Exceptions that will emit a warning when being caught. Defaults to
# "Exception"
overgeneral-exceptions=Exception
