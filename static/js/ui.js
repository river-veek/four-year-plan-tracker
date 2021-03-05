

function toggleLogin (name) {
	"""
	HEADER
	"""
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

  // for previous student send data back
 }

// Wrapper for main toggleLogin for when user inputs new student ID
function toggleLoginNew () {
	"""
	HEADER
	"""
  const input = document.getElementById('studentCreateInput').value
  return toggleLogin(input)
}

// Takes current option value - adds it to table
function addClass () {
	"""
	HEADER
	"""
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
    alert('Not an Option :)')
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
	"""
	HEADER
	"""
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
  }
}

function saveTable () {
	"""
	Function gets Table object and collects its rows cell by cell, then clears 
	table and can return data for a POST to backend
	"""
	
  // gets current table data and deletes it from table on page
  const theData = document.getElementById('course-rows').rows
  const tableData = []
  for (let x = 0; x < theData.length; x++) {
    const tmp = theData[x].children
    const current = []
    for (let v = 0; v < tmp.length; v++) { current.push(tmp[v].innerText) }
    tableData.push(current)
  }

  const table = document.getElementById('course-rows')
  const len = table.rows.length
  for (let z = 0; z < len; z++) { table.deleteRow(0) }

  return tableData
}

// returns Id being passed from new user 
function saveID () {
	return document.getElementById('studentCreateInput').value
}

// Used for case of existing user, passes Jinja value to POST and Sets up main page 
function existingUser(name){
	"""
	HEADER
	"""
	var stringName = {'login': name}
	console.log(stringName)
	toggleLogin(name)
	var stringName = {'login': name}
  $.ajax({
		type: "POST",
		url: '/forecast',
		data: JSON.stringify(stringName),
		contentType: 'application/json; charset=utf-8',
	  	success: function(data){
	  	//alert("Log in sent")
	  	console.log("login successfully")
	  	console.log("Success!")
	  	},
	  	error: function(request, error) {
		console.log(arguments)
		alert("Error: " + error)
	  	}
  	});
}

// All Ajax calls placed here for quick lookup and code alteration
$(document).ready(function() {
	$('#display').on('click', function() {
		const tableData = saveTable()
		var tblData = {'tableData': tableData}
		$.ajax({
			type: "POST",
			url: '/forecast',
			data: JSON.stringify(tblData),
			contentType: 'application/json; charset=utf-8',
	  		success: function(data){
	  		// alert('Saving... Ready to Display!')
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
		console.log(tblData)
		$.ajax({
			type: "POST",
			url: '/forecast',
			data: JSON.stringify(tblData),
			contentType: 'application/json; charset=utf-8',
	  		success: function(data){
	 		// alert('Saved Progress')
	  		console.log("saved successfully")
	  		console.log(data)
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
  			// alert("Log in sent")
  			console.log("login successfully")
  			console.log("Success!")
  			},
  			error: function(request, error) {
			console.log(arguments)
			alert("Error: " + error)
  			}
 		});
  	});
});

