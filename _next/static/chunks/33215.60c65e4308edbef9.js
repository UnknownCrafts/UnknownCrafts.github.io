(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[19117,33215],{29563:e=>{e.exports=function(e){return e&&e.__esModule?e:{default:e}},e.exports.__esModule=!0,e.exports.default=e.exports},33215:(e,s,t)=>{"use strict";var a=t(29563);Object.defineProperty(s,"__esModule",{value:!0}),s.default=void 0,s.default=a(t(82643)).default},82643:e=>{"use strict";function s(e){var s;e.languages.diff={coord:[/^(?:\*{3}|-{3}|\+{3}).*$/m,/^@@.*@@$/m,/^\d.*$/m]},Object.keys(s={"deleted-sign":"-","deleted-arrow":"<","inserted-sign":"+","inserted-arrow":">",unchanged:" ",diff:"!"}).forEach(function(t){var a=s[t],d=[];/^\w+$/.test(t)||d.push(/\w+/.exec(t)[0]),"diff"===t&&d.push("bold"),e.languages.diff[t]={pattern:RegExp("^(?:["+a+"].*(?:\r\n?|\n|(?![\\s\\S])))+","m"),alias:d,inside:{line:{pattern:/(.)(?=[\s\S]).*(?:\r\n?|\n)?/,lookbehind:!0},prefix:{pattern:/[\s\S]/,alias:/\w+/.exec(t)[0]}}}}),Object.defineProperty(e.languages.diff,"PREFIXES",{value:s})}e.exports=s,s.displayName="diff",s.aliases=[]}}]);