
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
		["Class, Days, Time", "Credits, Difficulty (out of 4)"],
		["CIS 422, WF, 1400-1600", "4 Credit Hours, 3"],
		["CIS 415, MWF, 0800-1000","3 Credit Hours, 2"]
	]
	
	let table = document.createElement('table');
	for(let row of tableArr)
	{
		table.insertRow();
		for(let cell of row){
			let newCell = table.rows[table.rows.length - 1].insertCell();
			newCell.textContent = cell;
		}
	}
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