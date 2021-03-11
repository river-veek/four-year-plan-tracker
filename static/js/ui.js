

function toggleLogin (name) {
  /**
	* @desc On users input, restructures DOM to present main functions used to create a four year plan 
	* @param string name - user's student Id number to be displayed
	* @return None
  */
  // get elements of DOM
  const main = document.getElementById('main-space')
  const add = document.getElementById('add')
  const save = document.getElementById('save')
  const displaybtn = document.getElementById('display')
  const remove = document.getElementById('remove')
  const dInfo = document.getElementById('helperDropdownInfo')
  const tInfo = document.getElementById('helperTableInfo')

  // Update the display for what student has been selected
  const currStudentText = document.getElementById('currStudentText')
  const currStudent = document.getElementById('currStudent')

  // Set display fields
  currStudent.innerText = name
  currStudentText.innerText = 'Current Student: '

  // Hide log-in
  main.style.display = 'none'

  // display main feature dropdowns
  add.style.display = 'inline'
  save.style.display = 'inline'
  remove.style.display = 'inline'
  displaybtn.style.display = 'inline'

  // display add/remove buttons
  document.getElementById('added-list').style.display = 'block'
  document.getElementById('button-row').style.display = 'inline-flex'
  dInfo.style.display = 'inline'
  tInfo.style.display = 'inline'
 }

function toggleLoginNewUser () {
  /**
	* @desc collects input of new user's Id, then passes it to toggleLogin. 	
    * @param None
	* @return None
  */
  const input = document.getElementById('studentCreateInput').value
  toggleLogin(input)
}

function addClass () {
  /**
	* @desc creates Table row and adds the user's current selection of Course, Term and Year to that row
    * @param None
	* @return None
  */
  // get Course Dropdown
  const courseOption = document.getElementById('courses')
  // save Course selected
  const cVal = courseOption.options[courseOption.selectedIndex].value
  // get Term Dropdown
  const termOption = document.getElementById('terms')
  // save Term selected
  const tVal = termOption.options[termOption.selectedIndex].value
  // get Year Dropdown
  const yearOption = document.getElementById('year')
  // save Year selected
  const yVal = yearOption.options[yearOption.selectedIndex].value
  // access table in DOM
  const table = document.getElementById('course-rows')

  // if Trying to add dummy value - display not an option
  if (cVal === 'Course Name' || tVal === 'Term' || yVal === 'Year') {
    showAlert("Error Adding Course: Could not find given course at specified Year and Term!", "alert-warning")
  } else {
    // else insert new row
    const row = table.insertRow()
    // assign class
    row.className = 'table-warning' // Example of how to set Bootstrap class dynamically
    // always add 3 cells as only inserting choice, term and year
    for (let x = 0; x < 3; x++) {
    // insert new cell into row - 0 indexed
      table.rows[table.rows.length - 1].insertCell()
    }
    const currRow = table.rows[table.rows.length - 1].cells
    // Set each cell to correct value;
    currRow[0].textContent = cVal
    currRow[1].textContent = tVal
    currRow[2].textContent = yVal
  }
}

function removeClass() {
  /**
	* @desc Finds and deletes Row containing the Course, Term and Year selected from the table 
    * @param None
	* @return None
  */
  // get Course Dropdown
  const courseOption = document.getElementById('courses')
  // save Course selected
  const cVal = courseOption.options[courseOption.selectedIndex].value
  // get Term Dropdown
  const termOption = document.getElementById('terms')
  // save Term selected
  const tVal = termOption.options[termOption.selectedIndex].value
  // get Year Dropdown
  const yearOption = document.getElementById('year')
  // save Year selected
  const yVal = yearOption.options[yearOption.selectedIndex].value
  // access table in DOM
  const table = document.getElementById('course-rows')
  // get # of rows
  const len = table.rows.length
  // if the table isn't empty
  if (len > 0) {
    let found = false
    let idx = 0
    // until found or gone through entire table
    while (!found && idx < len) {
    // get current row cell's values
      const currRow = table.rows[idx].cells
      // compare if this row is the correct one
      if (currRow[0].innerText === cVal && currRow[1].innerText === tVal && currRow[2].innerText === yVal) {
        found = true
        // set bool and delete row
     
        table.deleteRow(idx)
      } else { idx++ }
    }
    if(idx >= len && !found)
      { showAlert("Error Removing Course: Could not find given course at specified Year and Term!", "alert-warning")}
  }
}

function saveTable () {
  /**
	* @desc collects the data within the table to an List of Lists & clears table of data
    * @param None
	* @return List - List of Lists containing 3 indexes - Course, Term, Year
  */
  // gets current table data and deletes it from table on page
  const theData = document.getElementById('course-rows').rows
  // List to contain all the rows as lists
  const tableData = []
  for (let x = 0; x < theData.length; x++) {
	// get current Row
    const tmp = theData[x].children
    const current = []
    // push all the cells data into the temp
    for (let v = 0; v < tmp.length; v++) { current.push(tmp[v].innerText) }
    // push the List into the original List
    tableData.push(current)
  }
  // Clear the table of the data
  const table = document.getElementById('course-rows')
  const len = table.rows.length
  for (let z = 0; z < len; z++) { table.deleteRow(0) }

  return tableData
}


function saveID () {
  /**
	* @desc gets the input value the user enters for their student Id
    * @param None
	* @return string - studentId numbers
  */
	return document.getElementById('studentCreateInput').value
}


function showAlert(message, alerttype) {
  /**
	* @desc creates and inserts Bootstrap Alerts into HTML for 3 seconds, then removes it 
	* @param string message - Message to be displayed in Alert
	* @param string alerttype - will create type of alert depending on param input
	* @return div - Alert box lasting 3 seconds before disappearing
  */
  	// inserts alert div within the heading container, containing the alert message
	$('#heading').append( $('#heading').append(
	'<div id="alertdiv" class="alert alert-danger alert-dismissible fade show"' + alerttype + '">' + 
		'<a class="close" data-dismiss="alert" aria-label="close" >x</a>' + '<span>' + message +
		'</span>' + '</div>')
	);
	// sets alert box to remove itself after 3 seconds 
	setTimeout(function() {
		$('#alertdiv').remove();}, 3500);
}

 
function existingUser(name){
  /**
	* @desc sends data from jinja to flask using Ajax
	* @param string name - the students Id number being sent 
	* @return None
  */	
    var stringName = {'login': name}
	toggleLogin(name)
  $.ajax({
		type: "POST",
		url: '/forecast',
		data: JSON.stringify(stringName),
		contentType: 'application/json; charset=utf-8',
	  	success: function(data){
	  	console.log("login successfull!")
	  	
	  	},
	  	error: function(request, error) {
		console.log(arguments)
		alert("Error: " + error)
	  	}
  	});
}


$(document).ready(function() {
	/**
	  * @desc on document load, sets Ajax to send data - depending on which 
		button was pressed - with Ajax to flask 
	  * @return None
  	*/
	$('#display').on('click', function() {
		const tableData = saveTable()
		var tblData = {'tableData': tableData}
		$.ajax({
			type: "POST",
			url: '/forecast',
			data: JSON.stringify(tblData),
			contentType: 'application/json; charset=utf-8',
	  		success: function(data){
	  		document.write(data)
	  		console.log("Success!")
	  		},
	  		error: function(request, error) {
			console.log(arguments)
			alert("Error: " + error)
	  		}
  			});
  		});

  	$('#save').on('click', function() {
		const tableData = saveTable()
		var tblData = {'savedData': tableData}
		$.ajax({
			type: "POST",
			url: '/forecast',
			data: JSON.stringify(tblData),
			contentType: 'application/json; charset=utf-8',
	  		success: function(data){
	  		console.log("saved successfully")
	  		},
	  		error: function(request, error) {
			console.log(arguments)
			alert("Error: " + error)
	  		}
  		});
  	});

  	$('#newstudent').on('click', function() {
		var studentID = saveID()
		var studentData = {'login': studentID}
		$.ajax({
			type: "POST",
			url: '/forecast',
			data: JSON.stringify(studentData),
			contentType: 'application/json; charset=utf-8',
  			success: function(data){
  			console.log("Login successful")
  			},
  			error: function(request, error) {
			console.log(arguments)
			alert("Error: " + error)
  			}
 		});
  	});
});

