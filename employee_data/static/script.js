document.addEventListener("DOMContentLoaded", function() {
    // Function to handle employee creation form submission
    const createEmployeeForm = document.getElementById("createEmployeeForm");
    if (createEmployeeForm) {
        createEmployeeForm.addEventListener("submit", function(event) {
            event.preventDefault();
            
            const formData = new FormData(createEmployeeForm);
            fetch("/create_employee", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                createEmployeeForm.reset();
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    }

    // Function to handle employee deletion form submission
    const deleteEmployeeForm = document.getElementById("deleteEmployeeForm");
    if (deleteEmployeeForm) {
        deleteEmployeeForm.addEventListener("submit", function(event) {
            event.preventDefault();
            
            const formData = new FormData(deleteEmployeeForm);
            fetch("/delete_employee", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                deleteEmployeeForm.reset();
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    }

    // Function to handle employee checking form submission
    const checkEmployeeForm = document.getElementById("checkEmployeeForm");
    if (checkEmployeeForm) {
        checkEmployeeForm.addEventListener("submit", function(event) {
            event.preventDefault();
            
            const formData = new FormData(checkEmployeeForm);
            fetch("/check_employee", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(`Attendance: ${data.attendance}`);
                checkEmployeeForm.reset();
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    }
});
