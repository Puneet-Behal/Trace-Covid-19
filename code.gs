
var SPREADSHEET_ID='1jRfthUvnAiP4d9OzF6B7ZKyOLgg2cGNXygvy7dLS6Ow';
var SHEET_NAME = 'Track Covid-19';
var SHEET_NAME_2 = 'Cluster_Covid_19';

function doGet(request) {
   Logger.log(JSON.stringify(request));
  var callback = request.parameters.json;
  var sheet = "";
  var range = [];
  
  if(request.parameters.sheet == "markers"){
   sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME);
    range = sheet.getDataRange();
  }
  if(request.parameters.sheet == "clusters"){
     sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME_2);
     range = sheet.getDataRange();
  }
 // var secondSheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheets()[1];
  var json = range.getValues();
  
  return ContentService.createTextOutput(request.parameters.jsonp + '(' + JSON.stringify(json) + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
}

//function doGet(request) {
//  var response = UrlFetchApp.fetch('https://api.rootnet.in/covid19-in/unofficial/covid19india.org/travelhistory');
//  	var range = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME).getDataRange();
//    var sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME);
//  var secondSheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME_2);
// // var data =  Utilities.jsonParse(response.getContentText());
// // var data = JSON.parse(response.getContentText());
//  var myjson = JSON.parse(response);
// // var rows = [['source', 'google'], ['users', '378']]; // Sample data
//  var rows = []
//  for(var i=0; i<myjson.data.travel_history.length;i++){
//    var latlong_arr = myjson.data.travel_history[i].latlong.split(",")
//    rows = [[ myjson.data.travel_history[i].timefrom," ",myjson.data.travel_history[i].address,latlong_arr[0], latlong_arr[1], " ", " ", " ", " " ]]
//  	sheet.getRange(sheet.getLastRow()+1, 1, rows.length, rows[0].length).setValues(rows);
//  }
 //   return ContentService.createTextOutput(response.getContentText());
//}

//Snippets.prototype.appendValues = function(spreadsheetId, range,
//    valueInputOption, _values) {
//  // [START sheets_append_values]
//  var values = [
//    [
//      // Cell values ...
//    ]
//    // Additional rows ...
//  ];
//  // [START_EXCLUDE silent]
//  values = _values;
//  // [END_EXCLUDE]
//  var valueRange = Sheets.newRowData();
//  valueRange.values = values;
//
//  var appendRequest = Sheets.newAppendCellsRequest();
//  appendRequest.sheetId = spreadsheetId;
//  appendRequest.rows = [valueRange];
//
//  var result = Sheets.Spreadsheets.Values.append(valueRange, spreadsheetId, range, {
//    valueInputOption: valueInputOption
//  });
//  // [END sheets_append_values]
//  return result;
//};

//function setDataToTable(data) {
//	var range = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME).getDataRange();
//    var sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getSheetByName(SHEET_NAME);
// // var data =  Utilities.jsonParse(response.getContentText());
////  var data = JSON.parse(response.getContentText());
//  for (var i=1;i<data.length;i++) {
//    var rows = [data.travel_history[i][8], " ", data.travel_history[i][2]]; 
//    
//    sheet.getRange(sheet.getLatRow(), sheet.getLastColumn(), rows.length, rows[0].length).setValues(rows);
//  }
	
//}
