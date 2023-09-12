#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {}
	for (let key in dict) {
		if (newDict.hasOwnProperty(dict[key]))
			newDict[dict[key]].push(key)
		else
			newDict[dict[key]] = [key]
		/*newDict[dict[key]].push(key)*/
	}
console.log(newDict)
