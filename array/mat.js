async function runPy() {//async baki kaam chlta rahe jab tk yeh ho raha stoak gies on
    let pyodide = await loadPyodide();//wait un til it hjas ;loaded


// Install NumPy (if not already installed)
await pyodide.loadPackage("numpy");
//pythion fxn defination
pyodide.runPython(`
    import numpy as np
    def reshape_array(arr, rows, cols):
        npmt = np.array(arr)
        return npmt.reshape((rows, cols))

    def mtmul(arr1,arr2):
        ml= np.matmul(arr1, arr2)
        return ml.reshape((2,2))
        `);

        //user input ke liye
        let a1 = document.getElementById("userArrayInput").value;
        let jsa1 = a1.split(',').map(Number); //js conversion from user input
        let a2 = document.getElementById("userArrayInput2").value;
        let jsa2 = a2.split(',').map(Number); 
        let pymat1 = pyodide.toPy(jsa1);//py coversion
        let pymat2 = pyodide.toPy(jsa2);

        if (jsa1.length !== 4 || jsa2.length !== 4) {
        document.getElementById("output").textContent = "Error: Please enter 4 values for each matrix.";
        return;
    }

    let reshape_array = pyodide.globals.get('reshape_array');

// Reshape the first array to 2x2
let reshapedArray = reshape_array(pymat1, 2, 2);//python fxn ke andr python array passed

let reshapedArray2 = reshape_array(pymat2, 2, 2);
let mulmt = pyodide.globals.get('mtmul');

let result = mulmt(reshapedArray, reshapedArray2);

// Convert the reshaped array back to JavaScript for further  use
let resultArray = Array.from(result);  // Convert numpy array to regular JavaScript array

// Display the result
document.getElementById("output").textContent = `multiplied array: ${resultArray}`;
    //   document.getElementById("output").textContent = `multiplied array: hi \n${resultArray.map(row => row.join(", ")).join("\n")}`
      
      
    }