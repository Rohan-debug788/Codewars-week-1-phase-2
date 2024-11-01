var React = require("react");

function createElement(content, tag= 'div', props= {}) {
  // create a react element here
  return React.createElement(tag, props, content)
}

function createUnorderedList(list) { 
  // create a react unordered list with children list items created form the list argument
  return React.createElement(
    'ul', 
    null,
    list.map((x, index) =>
        React.createElement( 'li', {key: `x-${index}` }, x)
  )
 );   
}