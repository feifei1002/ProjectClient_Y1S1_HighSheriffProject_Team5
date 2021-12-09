$(document).ready(function () { // When the document load it runs this
    $('#applicantTable tr').each(function () { // It searchs each cell the table and performs the code below
        var current = this; // This stores the current cell that is searched
        $(this).closest('tr').find('td:first').addClass("appId"); // This adds a class to the first cell to identify it later
        $(this).find('td:contains("None")').each(function () { // This specifcally searches for cells that have no funding
            $(this).html("<p class='text-warning'>Needs moderator input</p>");
            $("#modMsg").html("<p class='text-warning'>There are applications that need moderator input: </p>");
            $('#requestedTable').append(current); // Appeds all of the following to a new table
        });
    });
    $('.vid').each(function () {
        var video = $(this).text();
        $(this).html("<video width='256' height='170' controls src="+ video +">Database Video</video>");
    });
    $('#waitTable .appId:first').each(function () {
        var applicantID = $(this).html(); // The following code simply creates the buttons buttons in html
        $(this).append("<form method='post' action='/acceptApplication'><input class='hiddenID' name='ID' type='text' value='0' style='display: none;'><input type='number' name='fundsToAdd' placeholder='Enter Funds to Award'><button type='submit' class='btn btn-outline-success'>Accept</button></form>");
        $(this).append("<form method='post' action='/declineApplication'><input class='hiddenID2' name='ID' type='text' value='0' style='display: none;'><button type='submit' class='btn btn-outline-danger'>Reject</button></form>");
        $('.hiddenID').attr("value", applicantID);
        $('.hiddenID2').attr("value", applicantID);
    });
    $('#waitReworkingTable .appId:first').each(function () {
        var applicantID = $(this).html(); // The following code simply creates the buttons buttons in html
        $(this).append("<form method='post' action='/acceptReworkingApplication'><input class='hiddenID' name='ID' type='text' value='0' style='display: none;'><input type='number' name='fundsToAdd' placeholder='Enter Funds to Award'><button type='submit' class='btn btn-outline-success'>Accept</button></form>");
        $(this).append("<form method='post' action='/declineReworkingApplication'><input class='hiddenID2' name='ID' type='text' value='0' style='display: none;'><button type='submit' class='btn btn-outline-danger'>Reject</button></form>");
        $('.hiddenID').attr("value", applicantID);
        $('.hiddenID2').attr("value", applicantID);
    });
});