import pandas as pd
import random

def fetch_mock_match_data(num_matches=100):
    # Simulating data pulled from a gaming API
    data = {
        'brawler_power_level': [random.randint(7, 11) for _ in range(num_matches)],
        'team_synergy_score': [random.randint(40, 100) for _ in range(num_matches)],
        'map_win_rate_pct': [round(random.uniform(40.0, 65.0), 1) for _ in range(num_matches)],
        'match_outcome': [random.choice([0, 1]) for _ in range(num_matches)] # 1 = Win
    }
    df = pd.DataFrame(data)
    df.to_csv('pvp_match_history.csv', index=False)
    print("Mock API data fetched and saved to pvp_match_history.csv")

if __name__ == "__main__":
    fetch_mock_match_data()
