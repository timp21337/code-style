/* The following Javascript file serves as the style guide for we7 */

//name your Javascript file with a camelCase name (.js), named after the primary object it returns, or primary function

//immediately executing function expression
//parenthesis around the function
//no space between function and ()
//space between () and {
(function() {
  //code goes in here to avoid polluting the global scope

  //always use semicolons
  //indent 2 spaces

  //no end of line comments
  //comment before the thing you are commenting on

  //single quote all strings, escaping where necessary

  //declare vars where it makes sense to do so, combining into one var statement
  //indent all variable names, on separate lines except for short unassigned at the end
  //indent objects and functions
  var
    property = 'hello I\'m a string',
    something = 'else',
    //no space after [ or before ]
    //space after comma
    array = ['one', 'two'],
    //no space before : but space after
    object = {
      foo: 'bar',
      baz: function() {
        return 'hiya!';
      }
    },
    //lower camelCase for variable names
    numValue = 42,
    //start with a $ for jQuery objects
    $document = $(document),
    except, like, these, size, options;

  //use upper case and underscores for constants
  var MAGIC_NUMBER = 3;

  //if you need to create a constructor function, use a named function and start its name with a capital letter
  function Mouse(length) {
    this.wiskers = length;
  }

  var aMouse = new Mouse(3);

  //space after control statements and semicolons
  //space around operators
  //no space inside parenthesis (or [] or {})
  //don't create functions inside loops
  //see also loops below
  for (var i = 0; i < array.length; i++) {
    out(i + 2);
  }

  //open curly brackets on the same line
  //close curly brackets on its own line
  //always use curly brackets
  var out = function O(number) {

    //always use === for comparison
    if (number === 1) {
      return 'yes';
    }

    //except when comparing to null (matches undefined too)
    if (number == null) {
      return 'no';
    }

    //use isNaN() to check for NaN (Nan === NaN returns false)
    if (isNaN(number)) {
      return 'what?';
    }
    else {
      //name your function only when it needs to call itself, and make the name short
      return O(number - 1);
    }

  };

  //advanced stuff

  //functions can have private state
  var hasPrivate = (function() {
    var num = 0;

    return function(name) {
      num += 1;
      return 'hello ' + name + '. I\'ve said hello ' + num + ' times';
    };
  })();

  hasPrivate('Me');
  // -> hello Me. I've said hello 1 times
  hasPrivate('You');
  // -> hello You. I've said hello 2 times

  //avoid using 'this' inside functions, as it can change depending on how the function is called
  //avoid creating and using constructors (a missed 'new' can cause havok)

  //avoid switch statements or multiple ifs when you can (ab)use objects instead

  var type = 'a';

  var typeName = {t: 'track', a: 'artist'}[type];

  //asynchronous calls should use deferreds
  //the deferred returned from asyncCall will be resolved with an error occasionally
  var asyncCall = function(param) {
    var deferred = Deferred();
    //pass functions, not strings to setTimeout
    setTimeout(function() {
      if (Math.random() < 0.9) {
        deferred.resolve({message: param});
      }
      else {
        deferred.resolve({error: 'whoops'});
      }
    }, 2000);
    return deferred.promise();
  };

  //use pipe to change the result or the state of a deferred when it is resolved
  var waitFor = asyncCall('something').pipe(function(result) {
    if (result.error) {
      //change the state (so fail is called below)
      return Deferred.reject(result.error);
    }

    //change the result
    return result.message.toUpperCase();
  });

  //multiple chained function calls start each on new line, indented
  waitFor
    .done(function(result) {
      //result will be 'SOMETHING'
    })
    .fail(function(result) {
      //will be called 1/10 times
      //result will be 'whoops'
    });

  //passing a function to a function
  withStuff(function() {
    //anything
  }, 'other', 'args');

  //passing more than one function to a function - indent
  withStuff(
    function() {

    },
    'other', 'args', 'inline',
    function() {

    }
  );

  //watch out! array.splice() requires two arguments in IE
  //this does nothing in IE, in other browsers it trims the array to the first element
  array.splice(1);
  //do this instead
  array.splice(1, 1/0); //where 1/0 evaluates to Infinity

  //don't use setInterval - use setTimeout with a named function and reschedule if needed
  setTimeout(function check() {
    if (isReady()) {
      doSomething();
    }
    else {
      setTimeout(check, 200);
    }
  }, 200);

  //if order doesn't matter loop backwards (slightly quicker and fewer characters)
  var arr = ['a','b'];
  var j = arr.length;
  while (j--) {
    somethingWith(arr[i]);
  }

  //or you can be functional (works with objects too)
  _.each(arr, doSomething);

  //creating a modified array from an array or object - use map
  var obj = {
    prop: 'one',
    other: 'two'
  };
  var newArrFromObj = _.map(obj, function(value, key) {
    return key + ' ' + value;
  });
  var newArrFromArr = _.map(arr, function(element, index) {
    return '[' + index + ']=' + element;
  });

  //ternary
  var q = bool ? 'yey' : 'nay';

  //coercion / casting
  //string
  var str = '' + numValue;

  //number
  var num = +str;

  //boolean
  var bool = !!num;

  //shortcuts - ideally UglifyJS would do these automatically
  //Infinity
  var inf = 1/0;

  //-Infinity
  var ninf = 1/-0;

  //NaN - although not shorter, should gzip better
  var notanumber = 0/0;

  //simple checks before doing something can be done with && (instead of if)
  object && fire(object);

  //setting a default value can be done with || (as long as null, undefined, '' or 0 are not supposed to be valid)
  size = size || 100;

  //defaults for objects (not a ternary because typeof null is 'object')
  options = (typeof options === 'object') && object || {size: 100};

  //or for getting a property - handles options or the property being unset
  size = options && options.size || 100;

  //one line assign if not set
  var topics = {};
  var getTopic = function(name) {
    return topics[name] || (topics[name] = {topicName: name});
  };

})();
//blank line at end of file (aides concatenation of files)
