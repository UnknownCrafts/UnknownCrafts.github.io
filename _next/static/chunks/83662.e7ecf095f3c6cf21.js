(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[83662,33196],{83662:function(e,n,t){"use strict";var r=t(64836);Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var o=r(t(39303));n.default=o.default},39303:function(e){"use strict";function n(e){var n,t,r,o;n=/\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\)/.source,t=/(?:\b\w+(?:<braces>)?|<braces>)/.source.replace(/<braces>/g,function(){return n}),r=e.languages.pascaligo={comment:/\(\*[\s\S]+?\*\)|\/\/.*/,string:{pattern:/(["'`])(?:\\[\s\S]|(?!\1)[^\\])*\1|\^[a-z]/i,greedy:!0},"class-name":[{pattern:RegExp(/(\btype\s+\w+\s+is\s+)<type>/.source.replace(/<type>/g,function(){return t}),"i"),lookbehind:!0,inside:null},{pattern:RegExp(/<type>(?=\s+is\b)/.source.replace(/<type>/g,function(){return t}),"i"),inside:null},{pattern:RegExp(/(:\s*)<type>/.source.replace(/<type>/g,function(){return t})),lookbehind:!0,inside:null}],keyword:{pattern:/(^|[^&])\b(?:begin|block|case|const|else|end|fail|for|from|function|if|is|nil|of|remove|return|skip|then|type|var|while|with)\b/i,lookbehind:!0},boolean:{pattern:/(^|[^&])\b(?:False|True)\b/i,lookbehind:!0},builtin:{pattern:/(^|[^&])\b(?:bool|int|list|map|nat|record|string|unit)\b/i,lookbehind:!0},function:/\b\w+(?=\s*\()/,number:[/%[01]+|&[0-7]+|\$[a-f\d]+/i,/\b\d+(?:\.\d+)?(?:e[+-]?\d+)?(?:mtz|n)?/i],operator:/->|=\/=|\.\.|\*\*|:=|<[<=>]?|>[>=]?|[+\-*\/]=?|[@^=|]|\b(?:and|mod|or)\b/,punctuation:/\(\.|\.\)|[()\[\]:;,.{}]/},o=["comment","keyword","builtin","operator","punctuation"].reduce(function(e,n){return e[n]=r[n],e},{}),r["class-name"].forEach(function(e){e.inside=o})}e.exports=n,n.displayName="pascaligo",n.aliases=[]},64836:function(e){e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports}}]);