document.addEventListener('DOMContentLoaded',domloaded,false);
function domloaded(){
    const canvas = document.getElementById('drawing');
    const context = canvas.getContext('2d');
    const sidesSlider = document.getElementById('sidesSlider');
    const palette = {"yellow":"#fff563", "darkGray":"#222b38"};
    const sidesNumber = document.getElementById('sidesNumber');
    const display = document.getElementById('display');

    const radius = 175;
    const angleArcRadius = 30;

    function init() {
        const sides = parseInt(sidesSlider.value, 10);
        const angle = 2 * Math.PI / sides;

        drawPolygon(350, 350, sides, angle);

        sidesNumber.textContent = sides;
        
        let outerEdgeLength = Math.tan(angle/2) * radius * 2;
        let outerCircumference = outerEdgeLength * sides;
        let innerEdgeLength = Math.sin(angle/2) * radius * 2;
        let innerCircumference = innerEdgeLength * sides;
        let piEstimate = ((outerCircumference + innerCircumference) / 2) / (radius * 2);
        display.textContent = "π ≈ " + piEstimate;
    }

    sidesSlider.addEventListener("change", init);

    function drawPolygon(x, y, sides, angle) {
        
        // Clear canvas
        context.clearRect(0, 0, canvas.width, canvas.height);

        // Line style
        context.shadowColor = "black";
        context.shadowBlur = 5;
        context.lineWidth = 2;
        context.strokeStyle = "white";
        
        // Draw circle
        context.beginPath();
        context.arc(350, 350, radius, - Math.PI/2, Math.PI * 1.5);
        context.closePath();
        context.stroke();
        
        // Line style
        context.strokeStyle = "#fff563";
        context.fillStyle = "#222b38"

        // Draw inner polygon
        context.beginPath();
        for (let i = 0; i < sides; i++) {
            let xx = x + radius * Math.cos(angle * i - Math.PI / 2);
            let yy = y + radius * Math.sin(angle * i - Math.PI / 2);
            context.lineTo(xx, yy);
        }
        context.closePath();
        context.fill();
        context.stroke();

        // Draw inner slice lines 
        context.beginPath();
        // for (let i = 0; i < sides; i++) {
        //     let xx = x + radius * Math.cos(angle * i - Math.PI / 2);
        //     let yy = y + radius * Math.sin(angle * i - Math.PI / 2);
        //     context.moveTo(350, 350);
        //     context.lineTo(xx, yy);
        // }
        // let xx = x + radius * Math.cos(angle * 0 - Math.PI / 2);
        // let yy = y + radius * Math.sin(angle * 0 - Math.PI / 2);
        // context.moveTo(350, 350);
        // context.lineTo(xx, yy);
        // context.closePath();
        // context.stroke();

        // Line style
        context.strokeStyle = "#fff563";

        // Draw outer polygon
        context.beginPath();
        for (let i = 0; i < sides; i++) {
            let a = Math.tan(angle/2) * radius;
            let outerRadius = Math.sqrt(a*a + radius*radius)
            let xx = x + outerRadius * Math.cos(angle * i - (Math.PI / 2) - angle/2);
            let yy = y + outerRadius * Math.sin(angle * i - (Math.PI / 2) - angle/2);
            context.lineTo(xx, yy);
        }
        context.closePath();
        context.stroke();

        // Draw outer slice lines 
        context.beginPath();
        for (let i = 0; i < sides; i++) {
            let a = Math.tan(angle/2) * radius;
            let outerRadius = Math.sqrt(a*a + radius*radius)
            let xx = x + outerRadius * Math.cos(angle * i - (Math.PI / 2) - angle/2);
            let yy = y + outerRadius * Math.sin(angle * i - (Math.PI / 2) - angle/2);
            context.moveTo(350, 350);
            context.lineTo(xx, yy);
        }
        context.closePath();
        context.stroke();

        // Draw angle arc
        // context.beginPath();
        // context.arc(350, 350, angleArcRadius, Math.PI*1.5 - angle/2, Math.PI * 1.5);
        // context.stroke();

        

    }

    init();
}