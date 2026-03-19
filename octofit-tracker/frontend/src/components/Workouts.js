
const Workouts = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const baseUrl = codespace
    ? `https://${codespace}-8000.app.github.dev`
    : 'http://localhost:8000';
  const endpoint = `${baseUrl}/api/workouts/`;
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched workouts:', results);
        console.log('API endpoint:', endpoint);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [endpoint]);

  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Workouts</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered align-middle">
            <thead className="table-light">
              <tr>
                {workouts.length > 0 && Object.keys(workouts[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {workouts.map((workout, idx) => (
                <tr key={workout.id || idx}>
                  {Object.values(workout).map((val, i) => (
                    <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
