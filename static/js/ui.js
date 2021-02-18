
function toggleShow() {
  document.getElementById('dropdown-list').classList.toggle('show')
}

function toggleLogin() {
	 var button = document.getElementById('log-in');
	 var add = document.getElementById('add');
	 var save = document.getElementById('save');
	 if(button.style.display === "none")
	 {
		 button.style.display = "inline-block";
		 var clist=document.getElementById('choice-list');
		 var tlist=document.getElementById('term-list');
		 var ylist=document.getElementById('year-list');
		 clist.remove();
		 tlist.remove();
		 ylist.remove();
		 
		 add.style.display = "none";
		 save.style.display = "none";
		 
		 }
	 else{
		 button.style.display = "none";
		 createLists()
		 add.style.display = "inline";
		 save.style.display = "inline";

	 }
	 //getElementsByClassName('functions').style.display='inline';
}

function createLists(){
	createCourseList()
	createTermList()
	createYearList()
	//addTexts()
	
}

function addTexts(){
	var h_1 = document.createElement('H4');
	h_1.setAttribute('class', 'term-list');
	var termText = document.createTextNode("Cources");
	h_1.appendChild(termText);
	var h_2 = document.createElement('H4');
	h_2.setAttribute('class', 'term-list');
	termText = document.createTextNode("Terms");
	h_2.appendChild(termText);
	var h_3 = document.createElement('H4');
	h_3.setAttribute('class', 'term-list');
	termText = document.createTextNode("Years");
	h_3.appendChild(termText);

	document.getElementById('lists').appendChild(h_1);
	document.getElementById('lists').appendChild(h_2);
	document.getElementById('lists').appendChild(h_3);
	
	}

function createCourseList(){
	var classesList = ["Courses", "210: Computer Science I","211: Computer Science II","212: Computer Science III","313: Intermediate Data Structures","314: Computer Organization",
	"315: Intermediate Algorithms","322: Introduction to Software Engineering","330: C/C++ & Unix","399: Applied Cryptography"]
	var list = document.createElement('select');
	list.name = "Courses";
	list.id="choice-list";
	list.class="c-list";
	for(const val of classesList){
		var option = document.createElement("option");
		option.value = val;
		option.text = val;
		list.appendChild(option);
	}
	document.getElementById('init').appendChild(list);
}

function createTermList() {
	var termList = ["Terms","Fall", "Winter", "Spring", "Summer"]
	var tlist = document.createElement('select');
	tlist.name = "Term";
	tlist.id="term-list";
	tlist.class="t-list";
	for(const val of termList){
		var option = document.createElement("option");
		option.value = val;
		option.text = val;
		tlist.appendChild(option);
	}
	document.getElementById('init').appendChild(tlist);
	
}

function createYearList(){
	var yearList = ["Year","1st","2nd","3rd","4th","5th"]
	var ylist = document.createElement('select');
	ylist.name = "Year";
	ylist.id="year-list";
	ylist.class="y-list";
	for(const val of yearList){
		var option = document.createElement("option");
		option.value = val;
		option.text = val;
		ylist.appendChild(option);
	}
	document.getElementById('init').appendChild(ylist);
}

function toggleMatrix (){
	var matrix = document.getElementById('class-list')
	if(matrix)
	{
		matrix.remove()
		var button = document.getElementById('log-in');
		button.style.display = 'inline-block';
	}
	var button = document.getElementById('log-in');
		button.style.display = 'inline-block';
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
	//table.setAttribute("display", "table");
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