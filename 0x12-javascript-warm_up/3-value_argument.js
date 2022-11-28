#!/usr/bin/node
argvV = require('node:process').argv;
argvLen = argvV.length;
if (argvLen <= 2){
    console.log('No argument');
} else{
    for (let index = 2; index < argvLen; index++) {
        console.log(argvV[index]);;
        
    }
}
