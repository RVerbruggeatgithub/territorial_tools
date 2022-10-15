function findAlphaNumb(num, next, nextnext) {
	console.log('find', num, next, nextnext)
	var m = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	var result = []
	var fullproc = ""
	
	// 4 digit handler?
	if (num[0] == 0 && num[1] != 0 && nextnext[0] != 0 && nextnext[1] == 0) {
		console.log("Handle as 4 digit!", num, next, nextnext)
	}
	
	
	for (A = 0; A < m.length; A++) {
		//converting ASCII codes to int
		var B = m.charCodeAt(A);
		
		if (B < 58) {
			kiwi = m[A]
		}
		else {
			if (B >= 91) {
				B -= 71
			}
			else {
				B -= 65
			}
			adjust = Math.floor(B / 10 + 1 / (2 * 10))
			kiwi = String(adjust) +""+ String(B - 10 * adjust)
		}
		if (kiwi == num) {
			result = `${m[A]}`;
			//console.log("found?" ,m[A])
		}
	}
	prev_len = result.length
	if (result.length == 0) {
	// if this occurs only take the first number
		qres = String(num).split("")
		result += `${qres[0]}`;
		fullproc = qres[1]
	}
	console.log(result, result.length, 'adjusted from length:', prev_len, 'num:', num, 'result:', result )
	return {"result" : result, "remainder" : fullproc}
}

function digitTize(arr) {
	var out = []
	var inp = arr
	for (q = 0; q < inp.length; q++) {
		stringgedInt = String(inp[q])
		tl = stringgedInt.length
		switch(tl) {
			case 1:	
				stringgedInt = "00"+stringgedInt
				break;
			case 2:
				stringgedInt = "0"+stringgedInt
				break;
			case 3:
				stringgedInt = stringgedInt
				break;
			default:
				stringgedInt = stringgedInt
				break;
		}
		tmp_arr = stringgedInt.split('')
		out = [...out, ...tmp_arr]
	}
	//print(out)
	return out
}

function convert_to_alphnum(digittizedString) {
	test_str = ""
	next = ""
	nextnext = ""
	converted_to_sets = digittizedString.join(",").replaceAll(",","")
	for (u = 0; u < converted_to_sets.length; u+=2) {
		if (u < converted_to_sets.length - 4) {
			nextnext = converted_to_sets[u+5]+""+converted_to_sets[u+6]
		}
		if (u < converted_to_sets.length - 2) {
			next = converted_to_sets[u+3]+""+converted_to_sets[u+4]
		}
		result = findAlphaNumb(converted_to_sets[u]+""+converted_to_sets[u+1], next, nextnext)
		 // {"result" : result, "remainder" : qres[1]}
		test_str += result.result
		if (result.remainder != "") {
			converted_to_sets = result.remainder+""+converted_to_sets
			
		}
		
	}
	return test_str
}

function converter(myArray) {
	res = digitTize(myArray)
	return convert_to_alphnum(res)
}

/*
use:
org_arr = []
console.log(converter(org_arr))
*/



