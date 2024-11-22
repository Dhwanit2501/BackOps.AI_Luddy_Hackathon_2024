class Dashboard {
  constructor() {
      this.messageLimit = 50; // Maximum number of messages to show
      this.activityUpdateInterval = null;
      this.initializeElements();
      this.initializeCharts();
      this.initializeCalendar();
      var today = new Date();
      var dd = String(today.getDate()).padStart(2, '0');
      var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
      var yyyy = today.getFullYear();
      var flag = false;

      if (flag == false){
        this.fetchStatsForGivenDay(dd).then((result) => {
          document.getElementById('count-div-header').innerHTML = `Overview for date: ${mm}/${dd}/${yyyy}`;
          this.initializeCountCharts(result);
        });
        flag = true;
      }
      // this.loadInitialData();
  }

  initializeCountCharts(result){
    var options = {
      series: [result.Inserted],  // Percentage value for the radial bar
      chart: {
          height: 200,
          type: 'radialBar',  // Radial bar chart type
      },
      colors: ['#004b23'],
      plotOptions: {
        radialBar: {
            hollow: {
                size: '60%',  // Size of the hollow center (creating a donut effect)
            },
            dataLabels: {
                name: {
                    color: 'white', // Color for the label (e.g., "INSERT")
                    fontSize: '16px', // Optional: Set font size for the label
                    fontFamily: "Cinzel"
                    
                },
                value: {
                    color: 'white', // Color for the percentage (e.g., "70")
                    fontSize: '20px', // Optional: Set font size for the percentage
                    fontFamily: "Cinzel",
                    formatter: function (){
                        return result.Inserted;
                    }
                },
            },
        },
      },
      labels: ['INSERT'],  // Label for the radial chart
    };

    var radialChartInstance = new ApexCharts(document.querySelector("#chart1"), options);
    radialChartInstance.render();

    var options = {
        series: [result.Updated],  // Percentage value for the radial bar
        chart: {
            height: 200,
            type: 'radialBar',  // Radial bar chart type
        },
        colors: ['#184e77'],
        plotOptions: {

            radialBar: {
                hollow: {
                    size: '60%',  // Size of the hollow center (creating a donut effect)
                },
                dataLabels: {
                    name: {
                        color: '#f8f7ff', // Color for the label (e.g., "INSERT")
                        fontSize: '16px', // Optional: Set font size for the label
                        fontFamily: "Cinzel"
                    },
                    value: {
                        color: '#f8f7ff', // Color for the percentage (e.g., "70")
                        fontSize: '20px', // Optional: Set font size for the percentage
                        fontFamily: "Cinzel",
                        formatter: function (){
                            return result.Updated;
                        }
                    },
                },
            },
        },
        labels: ['UPDATE'],  // Label for the radial chart
    };

    var radialChartInstance = new ApexCharts(document.querySelector("#chart2"), options);
    radialChartInstance.render();

    var options = {
        series: [result.Deleted],  // Percentage value for the radial bar
        chart: {
            height: 200,
            type: 'radialBar',  // Radial bar chart type
        },
        colors: ['#9d0208'],
        plotOptions: {

            radialBar: {
                hollow: {
                    size: '60%',  // Size of the hollow center (creating a donut effect)
                },
                dataLabels: {
                    name: {
                        color: '#f8f7ff', // Color for the label (e.g., "INSERT")
                        fontSize: '16px', // Optional: Set font size for the label
                        fontFamily: "Cinzel"
                    },
                    value: {
                        color: '#f8f7ff', // Color for the percentage (e.g., "70")
                        fontSize: '20px', // Optional: Set font size for the percentage
                        fontFamily: "Cinzel",
                        formatter: function (){
                            return result.Deleted;
                        }
                    },
                },
            },
        },
        labels: ['DELETE'],  // Label for the radial chart
    };

    var radialChartInstance = new ApexCharts(document.querySelector("#chart3"), options);
    radialChartInstance.render();

    var total = result.Inserted + result.Updated + result.Deleted
    var options = {
      series: [total],  // Percentage value for the radial bar
      chart: {
          height: 200,
          type: 'radialBar',  // Radial bar chart type
      },
      colors: ['#2b2a2a'],
      plotOptions: {
        radialBar: {
            hollow: {
                size: '60%',  // Size of the hollow center (creating a donut effect)
            },
            dataLabels: {
                name: {
                    color: '#f8f7ff', // Color for the label (e.g., "INSERT")
                    fontSize: '16px', // Optional: Set font size for the label
                    fontFamily: "Cinzel"
                },
                value: {
                    color: '#f8f7ff', // Color for the percentage (e.g., "70")
                    fontSize: '20px', // Optional: Set font size for the percentage
                    fontFamily: "Cinzel",
                    formatter: function (){
                        return total
                    }
                },
            },
        },
      },
      labels: ['TOTAL'],  // Label for the radial chart
    };

    var radialChartInstance = new ApexCharts(document.querySelector("#chart4"), options);
    radialChartInstance.render();
  }

  initializeElements() {
      // Overview metrics
      this.totalQueriesElement = document.getElementById('totalQueries');
      this.avgResponseTimeElement = document.getElementById('avgResponseTime');
      this.successRateElement = document.getElementById('successRate');
      this.randomvizElement = document.getElementById('RandomFact');

      // Chat elements
      this.userInput = document.getElementById('userInput');
      this.sendBtn = document.getElementById('sendBtn');
      // this.voiceBtn = document.getElementById('voiceBtn');
      this.chatMessages = document.getElementById('chatMessages');
  }

  initializeCharts() {
      // Activity Chart
      this.fetchPastSevenDaysCount().then((result) => {
        const ctx = document.getElementById('activityChart').getContext('2d');
        this.activityChart = new Chart(ctx, {
          type: "bar",
          data: {
            labels: result.date,
            datasets: [
              {
                label: "Queries",
                data: result.count,
                backgroundColor: "#BA5370",
                borderColor: "#BA5370",
                borderWidth: 1,
                fontFamily: "Cinzel",
              },
            ],
          },
          options: {
            scales: {
              x: {
                grid: {
                  color: "#f8f7ff", // Color of the grid lines for the x-axis
                  lineWidth: 1, // Thickness of the grid lines
                },
                ticks: {
                  color: "#f8f7ff", // Color of the labels for the x-axis
                  font: {
                    family: "Cinzel", // Font family for y-axis labels
                    size: 12, // Font size for y-axis labels
                    weight: "bold", // Optional: Font weight for y-axis labels
                  },
                },
              },
              y: {
                beginAtZero: true,
                max: 3,
                ticks: {
                  stepSize: 1,
                  color: "#f8f7ff", // Color of the labels for the y-axis
                  font: {
                    family: "Cinzel", // Font family for y-axis labels
                    size: 12, // Font size for y-axis labels
                    weight: "bold", // Optional: Font weight for y-axis labels
                  },
                },
                grid: {
                  color: "#f8f7ff", // Color of the grid lines for the y-axis
                  lineWidth: 1, // Thickness of the grid lines
                },
              },
            },
            plugins: {
              legend: {
                labels: {
                  color: "#f8f7ff", // Color for the "Queries" label
                  font: {
                    size: 14, // Font size for the legend label
                    weight: "bold", // Font weight for the legend label
                    family: "Cinzel",
                  },
                },
              },
            },
          },
        });
      });
  }

  async fetchPastSevenDaysCount(){
    try {
      const response = await fetch("http://127.0.0.1:8000/get-past-day-log-stats?days=7", {
        method: 'GET',
        headers: {
          'Accept': 'application/json'
        }
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching past day log stats:', error);
    }
  }

  async fetchStatsForGivenDay(day){
    var today = new Date();
    var month = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var year = today.getFullYear();
    try {
      const response = await fetch(`http://127.0.0.1:8000/get-log-stats/${year}/${month}/${day}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching log stats:', error);
    }
  }

  // Clean up method to prevent memory leaks
  destroy() {
      if (this.activityUpdateInterval) {
          clearInterval(this.activityUpdateInterval);
      }
      if (this.activityChart) {
          this.activityChart.destroy();
      }
  }

  initializeCalendar() {
      const calendar = document.getElementById('calendar');
      const currentDate = new Date();
      const month = currentDate.toLocaleString('default', { month: 'long' });
      
      // Create calendar header
      const header = document.createElement('div');
      header.className = 'header';
      header.textContent = month;
      calendar.appendChild(header);

      // Create days grid
      const daysContainer = document.createElement('div');
      daysContainer.className = 'days';
      
      // Add days
      const daysInMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0).getDate();
      for (let i = 1; i <= daysInMonth; i++) {
          const day = document.createElement('div');
          day.className = 'day';
          day.addEventListener('click', function() {
            this.handleClick(i);
          }.bind(this));
          day.textContent = i;
          daysContainer.appendChild(day);
      }
      
      calendar.appendChild(daysContainer);
  }

  handleClick(day){
    document.querySelector("#chart1").innerHTML = '';
    document.querySelector("#chart2").innerHTML = '';
    document.querySelector("#chart3").innerHTML = '';
    document.querySelector("#chart4").innerHTML = '';

    var today = new Date();
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    document.getElementById('count-div-header').innerHTML = `Overview for date: ${mm}/${day}/${yyyy}`;

    this.fetchStatsForGivenDay(day).then((result) => {
      this.initializeCountCharts(result);
    });
  }
}


// Initialize dashboard when DOM is loaded and handle cleanup
let dashboardInstance;
document.addEventListener('DOMContentLoaded', () => {
  dashboardInstance = new Dashboard();
});

window.addEventListener('beforeunload', () => {
  if (dashboardInstance) {
      dashboardInstance.destroy();
  }
});