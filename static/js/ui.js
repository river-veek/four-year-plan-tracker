
function toggleShow() {
  document.getElementById('dropdown-list').classList.toggle('show')
}

function toggleButton() {
	 var button = document.getElementById('log-in');
	 if(button.style.display === "none")
	 {button.style.display = "inline-block";}
	 else{button.style.display = "none";}
}

function classInfo (id) {
	toggleShow ()
	toggleButton()
	//var currentSpace = document.getElementById('init')
	buildMatrix(id)

}
window.onclick = function (event) {
  if (!event.target.matches('.dropbtn')) {
    const dropdowns = document.getElementsByClassName('dropdown-content')
    for (let i = 0; i < dropdowns.length; i++) {
      const openDropdown = dropdowns[i]
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show')
      }
    }
  }
}


function buildMatrix(id)
{
	/*
	future reference - possibly iterate through students class list and insert them
	into Matrix and create on page
	*/
	var tableArr=[
		["Fall 2019","Days","Time","Credits", "Difficulty"],
		//["Class, Days, Time", "Credits, Difficulty (out of 4)"],
		["CIS 422", "WF", "1400-1600", "4","an L"],
		["CIS 415", "MWF", "0800-1000","3", "an L"],
		["CIS 212", "MWThF", "1200-1400", "2", "a Win"],
		["Winter 2020","Days","Time","Credits","Difficulty"],
		["CIS 407", "WF", "1400-1600", "4","an L"],
		["CIS 410", "MWF", "1000-1200","3", "an L"],
		["CIS 314", "MWThF", "1800-0200", "2", "a Win"],
		["Spring 2020","Days","Time","Credits","Difficulty"],
		["CIS 425", "MThF", "1530-1630", "3", "a Win"],
		["CIS 110", "MWF", "0230-0400", "3", "a Win"],
		["Summer 2020","Days","Time","Credits","Difficulty"],
		["","","","",""]
		//["CIS 410", "MTWF", "0830-1000", "3", "a Win"]		
	]
	//Create table
	let table = document.createElement('table');
	table.setAttribute("id", "class-list");
	//loop through each sub array in tableArr
	for(let row of tableArr)
	{
		//Create new Rows
		table.insertRow();
		//for each index of subarray 
		for(let cell of row){
			//create cell in row and add subarray value into cell
			let newCell = table.rows[table.rows.length - 1].insertCell();
			newCell.textContent = cell;
		}
	}
	//Need to go through and find row[0] == "Fall" | "Spring" | "Summer" | "Winter" ? 
	// More research into dealing with Tables, find possible work around instead of brute force search 
	//for(let x = 0; x < table.rows.length; x++)
	//{
	//	console.log(table.rows);
	//}
	
	
	document.body.appendChild(table);
	
	
	//for(let x = 0; x < 10; x++)
	//{
	//	tableArr.push(["row " + x])
	//}
	//console.log(tableArr.length)
	//for(let x = 0; x < tableArr.length; x++)
	//{
	//	console.log(tableArr)
		//}	
}