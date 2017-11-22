var pythonjs = require('python-js');

var code = pythonjs.translator.to_javascript( my_python_code ) // output javascript
eval( code )  // runs the javascript output server side within nodejs

// experimental backends
var code = pythonjs.translator.to_dart( my_python_code )       // output dart
var code = pythonjs.translator.to_coffee( my_python_code )     // output coffeescript
var code = pythonjs.translator.to_lua( my_python_code )        // output lua
var code = pythonjs.translator.to_visjs( my_python_code )      // output a graph for vis.js

// the runtime required on the client side by the javascript and coffee backends
var header = pythonjs.runtime.javascript