
function toggleShow() {
  document.getElementById('dropdown-list').classList.toggle('show');
}

function toggleLogin() {
	 var button = document.getElementById('log-in');
	 var add = document.getElementById('add');
	 var save = document.getElementById('save');
	 var displaybtn = document.getElementById('display');
	 var remove = document.getElementById('remove');

	button.style.display = "none";
    createLists()
    add.style.display = "inline";
    save.style.display = "inline";
	remove.style.display ="inline";
    displaybtn.style.display = "inline";
	//getElementsByClassName('functions').style.display='inline';
}

function createLists(){
	createCourseList()
	createTermList()
	createYearList()
	//addTexts()
	
}


//Takes current option value - adds it to table
function addClass()
{
	//get the current option values selected
	let currCourse = document.getElementById("choice-list");
	let currTerm = document.getElementById("term-list");
	let currYear = document.getElementById("year-list");
	//get table
	let table = document.getElementById('added-list');
	//insert new row
	table.insertRow();
	//always add 3 cells as only inserting choice, term and year
	for(let x = 0; x < 3; x++)
	{	//insert new cell into row
	    table.rows[table.rows.length - 1].insertCell();
	}
	let currRow = table.rows[table.rows.length - 1].cells
	//Set each cell to correct value;
	currRow[0].textContent = currCourse.value;
	currRow[1].textContent = currYear.value;
	currRow[2].textContent = currTerm.value;
}

//Builds course list for now - used for testing
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
//Builds term list for now - used for testing
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
//Builds year list for now - used for testing
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

//toggles dropdown for log in
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


