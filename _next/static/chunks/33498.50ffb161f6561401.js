(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[12102,16403,33498],{29563:e=>{e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports},33498:(e,t,n)=>{"use strict";var a=n(29563);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0,t.default=a(n(40038)).default},40038:(e,t,n)=>{"use strict";var a=n(44602);function r(e){e.register(a),function(e){for(var t=/[^<()"']|\((?:<expr>)*\)|<(?!#--)|<#--(?:[^-]|-(?!->))*-->|"(?:[^\\"]|\\.)*"|'(?:[^\\']|\\.)*'/.source,n=0;n<2;n++)t=t.replace(/<expr>/g,function(){return t});t=t.replace(/<expr>/g,/[^\s\S]/.source);var a={comment:/<#--[\s\S]*?-->/,string:[{pattern:/\br("|')(?:(?!\1)[^\\]|\\.)*\1/,greedy:!0},{pattern:RegExp(/("|')(?:(?!\1|\$\{)[^\\]|\\.|\$\{(?:(?!\})(?:<expr>))*\})*\1/.source.replace(/<expr>/g,function(){return t})),greedy:!0,inside:{interpolation:{pattern:RegExp(/((?:^|[^\\])(?:\\\\)*)\$\{(?:(?!\})(?:<expr>))*\}/.source.replace(/<expr>/g,function(){return t})),lookbehind:!0,inside:{"interpolation-punctuation":{pattern:/^\$\{|\}$/,alias:"punctuation"},rest:null}}}}],keyword:/\b(?:as)\b/,boolean:/\b(?:false|true)\b/,"builtin-function":{pattern:/((?:^|[^?])\?\s*)\w+/,lookbehind:!0,alias:"function"},function:/\b\w+(?=\s*\()/,number:/\b\d+(?:\.\d+)?\b/,operator:/\.\.[<*!]?|->|--|\+\+|&&|\|\||\?{1,2}|[-+*/%!=<>]=?|\b(?:gt|gte|lt|lte)\b/,punctuation:/[,;.:()[\]{}]/};a.string[1].inside.interpolation.inside.rest=a,e.languages.ftl={"ftl-comment":{pattern:/^<#--[\s\S]*/,alias:"comment"},"ftl-directive":{pattern:/^<[\s\S]+>$/,inside:{directive:{pattern:/(^<\/?)[#@][a-z]\w*/i,lookbehind:!0,alias:"keyword"},punctuation:/^<\/?|\/?>$/,content:{pattern:/\s*\S[\s\S]*/,alias:"ftl",inside:a}}},"ftl-interpolation":{pattern:/^\$\{[\s\S]*\}$/,inside:{punctuation:/^\$\{|\}$/,content:{pattern:/\s*\S[\s\S]*/,alias:"ftl",inside:a}}}},e.hooks.add("before-tokenize",function(n){var a=RegExp(/<#--[\s\S]*?-->|<\/?[#@][a-zA-Z](?:<expr>)*?>|\$\{(?:<expr>)*?\}/.source.replace(/<expr>/g,function(){return t}),"gi");e.languages["markup-templating"].buildPlaceholders(n,"ftl",a)}),e.hooks.add("after-tokenize",function(t){e.languages["markup-templating"].tokenizePlaceholders(t,"ftl")})}(e)}e.exports=r,r.displayName="ftl",r.aliases=[]},44602:e=>{"use strict";function t(e){!function(e){function t(e,t){return"___"+e.toUpperCase()+t+"___"}Object.defineProperties(e.languages["markup-templating"]={},{buildPlaceholders:{value:function(n,a,r,o){if(n.language===a){var i=n.tokenStack=[];n.code=n.code.replace(r,function(e){if("function"==typeof o&&!o(e))return e;for(var r,s=i.length;-1!==n.code.indexOf(r=t(a,s));)++s;return i[s]=e,r}),n.grammar=e.languages.markup}}},tokenizePlaceholders:{value:function(n,a){if(n.language===a&&n.tokenStack){n.grammar=e.languages[a];var r=0,o=Object.keys(n.tokenStack);!function i(s){for(var u=0;u<s.length&&!(r>=o.length);u++){var l=s[u];if("string"==typeof l||l.content&&"string"==typeof l.content){var p=o[r],c=n.tokenStack[p],f="string"==typeof l?l:l.content,g=t(a,p),d=f.indexOf(g);if(d>-1){++r;var k=f.substring(0,d),b=new e.Token(a,e.tokenize(c,n.grammar),"language-"+a,c),m=f.substring(d+g.length),x=[];k&&x.push.apply(x,i([k])),x.push(b),m&&x.push.apply(x,i([m])),"string"==typeof l?s.splice.apply(s,[u,1].concat(x)):l.content=x}}else l.content&&i(l.content)}return s}(n.tokens)}}}})}(e)}e.exports=t,t.displayName="markupTemplating",t.aliases=[]}}]);