(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[40587,76489],{29563:e=>{e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports},65077:e=>{"use strict";function n(e){!function(e){function n(e,n){return e.replace(/<<(\d+)>>/g,function(e,r){return"(?:"+n[+r]+")"})}function r(e,r,t){return RegExp(n(e,r),t||"")}var t=RegExp("\\b(?:"+"Adj BigInt Bool Ctl Double false Int One Pauli PauliI PauliX PauliY PauliZ Qubit Range Result String true Unit Zero Adjoint adjoint apply as auto body borrow borrowing Controlled controlled distribute elif else fail fixup for function if in internal intrinsic invert is let mutable namespace new newtype open operation repeat return self set until use using while within".trim().replace(/ /g,"|")+")\\b"),a=/\b[A-Za-z_]\w*\b/.source,s=n(/<<0>>(?:\s*\.\s*<<0>>)*/.source,[a]),i={keyword:t,punctuation:/[<>()?,.:[\]]/},o=/"(?:\\.|[^\\"])*"/.source;e.languages.qsharp=e.languages.extend("clike",{comment:/\/\/.*/,string:[{pattern:r(/(^|[^$\\])<<0>>/.source,[o]),lookbehind:!0,greedy:!0}],"class-name":[{pattern:r(/(\b(?:as|open)\s+)<<0>>(?=\s*(?:;|as\b))/.source,[s]),lookbehind:!0,inside:i},{pattern:r(/(\bnamespace\s+)<<0>>(?=\s*\{)/.source,[s]),lookbehind:!0,inside:i}],keyword:t,number:/(?:\b0(?:x[\da-f]+|b[01]+|o[0-7]+)|(?:\B\.\d+|\b\d+(?:\.\d*)?)(?:e[-+]?\d+)?)l?\b/i,operator:/\band=|\bor=|\band\b|\bnot\b|\bor\b|<[-=]|[-=]>|>>>=?|<<<=?|\^\^\^=?|\|\|\|=?|&&&=?|w\/=?|~~~|[*\/+\-^=!%]=?/,punctuation:/::|[{}[\];(),.:]/}),e.languages.insertBefore("qsharp","number",{range:{pattern:/\.\./,alias:"operator"}});var u=function(e,n){for(var r=0;r<2;r++)e=e.replace(/<<self>>/g,function(){return"(?:"+e+")"});return e.replace(/<<self>>/g,"[^\\s\\S]")}(n(/\{(?:[^"{}]|<<0>>|<<self>>)*\}/.source,[o]),0);e.languages.insertBefore("qsharp","string",{"interpolation-string":{pattern:r(/\$"(?:\\.|<<0>>|[^\\"{])*"/.source,[u]),greedy:!0,inside:{interpolation:{pattern:r(/((?:^|[^\\])(?:\\\\)*)<<0>>/.source,[u]),lookbehind:!0,inside:{punctuation:/^\{|\}$/,expression:{pattern:/[\s\S]+/,alias:"language-qsharp",inside:e.languages.qsharp}}},string:/[\s\S]+/}}})}(e),e.languages.qs=e.languages.qsharp}e.exports=n,n.displayName="qsharp",n.aliases=["qs"]},76489:(e,n,r)=>{"use strict";var t=r(29563);Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0,n.default=t(r(65077)).default}}]);