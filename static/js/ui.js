
function toggleShow() {
  document.getElementById('dropdown-list').classList.toggle('show');
}

function toggleLogin() {
	 var button = document.getElementById('log-in');
	 var add = document.getElementById('add');
	 var save = document.getElementById('save');
	 var displaybtn = document.getElementById('display');
	 var remove = document.getElementById('remove');
	 if(button.style.display === "none") {
		 button.style.display = "inline-block";
		 var clist=document.getElementById('choice-list');
		 var tlist=document.getElementById('term-list');
		 var ylist=document.getElementById('year-list');
		 var matr = document.getElementById('matrix');
		 matr.remove();
		 clist.remove();
		 tlist.remove();
		 ylist.remove();

		 add.style.display = "none";
		 save.style.display = "none";
		 remove.style.display ="none";
		 displaybtn.style.display = "none";
	 }
	 else {
		 button.style.display = "none";
		 createLists()
		 add.style.display = "inline";
		 save.style.display = "inline";
		 remove.style.display ="inline";
		 displaybtn.style.display = "inline";

	 }
	 //getElementsByClassName('functions').style.display='inline';
}

function createLists(){
	createCourseList()
	createTermList()
	createYearList()
	//addTexts()

}

function demoAddClass(){
	// Should be populating based on the dropdown info (not doing that yet)
	arr = [
	["Courses Added"],
	["210: Computer Science I"]
	]

	let prev = document.getElementById('matrix');
	if(prev)
	{
		prev.remove();
	}
	let table = document.createElement('table');
	table.setAttribute("id", "matrix");
	//table.setAttribute("display", "table");
	//loop through each sub array in tableArr
	for(let row of arr)
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
	//ID use #~
	const dropdownloc =document.querySelector('#init');
	dropdownloc.parentNode.insertBefore(table, dropdownloc);
	//document.body.appendChild(table);

}

function createCourseList(){
	// Populate from our Python data structures in the future
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
	//ID is useless for now
	toggleShow ()
	toggleButton()
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

function demoRemoveClass(){
   let mat = document.getElementById('matrix');
   mat.deleteRow(1);
   let len = mat.rows.length;
   console.log(len);
   if(len == 1)
   	{
	   	arr = ["No Courses Added"]
	   	mat.insertRow().insertCell(0).textContent = arr[0];
	   	mat.deleteRow(0);
	}
}



function buildMatrix(id)
{
	/*
	future reference - possibly iterate through students class list and insert them
	into Matrix and create on page
	*/
	var prevtable = document.getElementById('matrix');
	prevtable.remove();
	var tableArr=[
		["Courses","Term","Year"],
		//["Class, Days, Time", "Credits, Difficulty (out of 4)"],
		["210: Computer Science I", "Fall", "1st"]
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
	document.body.appendChild(table);
}
