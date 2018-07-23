// Update the trading chart with new data
function drawTradingChart(newData) {
          var tradingChart = document.getElementById('tradingChart');
          // Plotly.restyle(Bar, 'x', [newdata.x])
          //  Plotly.restyle(Bar, 'y', [newdata.y])
          }

function drawFundamentals(ticker) {
          var valueChart = document.getElementById('tradingChart');
          var analysisTable = document.getElementById('analysisTable');
          //get data
          route="/api/fundamentals?ticker="+ticker;
          Plotly.d3.json(route, function(error, response) {
                  if (error) return console.warn(error);
                  console.log()

                 });
              }
      
// Get new data whenever the dropdown selection changes and draw the dashboard
function drawDashboard(ticker) {
          console.log(ticker);
          drawTradingChart(ticker);
          drawFundamentals(ticker);
          buildPlot();
          }

