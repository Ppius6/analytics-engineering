"""
LendSight Real Estate Finance Data Generator

Generates realistic data for a real estate loan portfolio dashboard including:
- Recent transactions
- Portfolio metrics
- Property type analytics
- Client risk profiles
"""

import json
import csv
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
import os


class LendSightDataGenerator:
    def __init__(self, seed: int = 42):
        """Initialize the data generator with a random seed for reproducibility."""
        random.seed(seed)

        # Configuration
        self.property_types = ["Retail Mall", "Mixed-Use", "Apartment Block",
                               "Office Space", "Warehouse"]
        self.client_prefixes = [
            "Willis", "Rogers", "Lee", "Vasquez", "Collins", "Bates",
            "Hernandez", "Jones", "Morrison", "Ross", "Jordan",
            "Thomas", "Lewis", "Bray", "Bender", "Brown", "Mitchell", "Anderson",
            "Chavez", "Morgan", "Klein", "Flores", "Smith", "Johnson", "Williams",
            "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas",
            "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
            "Robinson", "Clark", "Rodriguez", "Lewis", "Walker", "Hall", "Allen",
            "Young", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams",
            "Baker", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner",
            "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart",
            "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy",
            "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward",
            "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks",
            "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross"
        ]
        self.suffixes = ["LLC", "Group", "Ltd", "Inc", "& Sons", "and Sons", "Associates", "Partners", "Corp", "Enterprises"]
        self.regions = {
            "New York": 0.29,
            "California": 0.27,
            "Illinois": 0.18,
            "Florida": 0.12,
            "Texas": 0.15
        }
        self.emails_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "company.biz", "business.com"]

    def generate_client_name(self) -> str:
        """Generate a random client company name."""
        if random.random() < 0.3:  # 30% chance of combined name
            name1 = random.choice(self.client_prefixes)
            name2 = random.choice(self.client_prefixes)
            while name2 == name1:
                name2 = random.choice(self.client_prefixes)
            connector = random.choice(["-", " & ", ", "])
            return f"{name1}{connector}{name2} {random.choice(self.suffixes)}"
        else:
            return f"{random.choice(self.client_prefixes)} {random.choice(self.suffixes)}"

    def generate_email(self, client_name: str) -> str:
        """Generate a random email address."""
        username = random.choice(self.client_prefixes).lower() + str(random.randint(10, 99))
        domain = random.choice(self.emails_domains)
        return f"{username}@{domain}"

    def calculate_monthly_payment(self, principal: float, annual_rate: float, term_months: int) -> float:
        """Calculate monthly payment using amortization formula."""
        if annual_rate == 0:
            return principal / term_months

        monthly_rate = annual_rate / 100 / 12
        payment = principal * (monthly_rate * (1 + monthly_rate)**term_months) / \
                  ((1 + monthly_rate)**term_months - 1)
        return round(payment, 2)

    def calculate_outstanding_balance(self, principal: float, annual_rate: float,
                                     term_months: int, payments_made: int) -> float:
        """Calculate remaining loan balance after specified payments."""
        if payments_made >= term_months:
            return 0.0

        if annual_rate == 0:
            return principal - (principal / term_months * payments_made)

        monthly_rate = annual_rate / 100 / 12
        monthly_payment = self.calculate_monthly_payment(principal, annual_rate, term_months)

        # Calculate remaining balance using amortization formula
        remaining_balance = principal * (1 + monthly_rate)**payments_made - \
                           monthly_payment * (((1 + monthly_rate)**payments_made - 1) / monthly_rate)

        return round(max(0, remaining_balance), 2)

    def generate_clients(self, count: int = 100) -> List[Dict[str, Any]]:
        """Generate client data for specified number of clients."""
        clients = []
        start_date = datetime.now() - timedelta(days=730)  # 2 years back
        current_date = datetime.now()

        for i in range(count):
            client_name = self.generate_client_name()

            # Generate loan details
            days_ago = random.randint(0, 730)
            loan_date = start_date + timedelta(days=days_ago)

            # Determine loan status
            status_rand = random.random()
            if status_rand < 0.76:
                status = "Active"
            elif status_rand < 0.86:
                status = "Late Payment"
            else:
                status = "Paid Off"

            # Loan parameters
            loan_amount = random.randint(15_000_000, 300_000_000)
            interest_rate = round(random.uniform(8.5, 15.5), 2)
            term_months = random.choice([36, 48, 60, 72, 84])

            # Calculate monthly payment
            monthly_payment = self.calculate_monthly_payment(loan_amount, interest_rate, term_months)

            # Calculate payments made based on time elapsed
            months_elapsed = max(0, (current_date.year - loan_date.year) * 12 +
                               (current_date.month - loan_date.month))

            # Determine payments made based on status
            if status == "Paid Off":
                payments_made = term_months  # Loan is fully paid
            elif status == "Late Payment":
                # Late payment: made fewer payments than elapsed time
                payments_made = max(0, months_elapsed - random.randint(1, 3))
            else:  # Active
                # Active: payments on schedule
                payments_made = min(months_elapsed, term_months)

            # Calculate outstanding balance
            outstanding_balance = self.calculate_outstanding_balance(
                loan_amount, interest_rate, term_months, payments_made
            )

            client = {
                "client_id": f"C{str(i + 1).zfill(4)}",
                "client_name": client_name,
                "loan_id": f"L{str(i + 1).zfill(4)}",
                "property_type": random.choice(self.property_types),
                "region": random.choices(
                    list(self.regions.keys()),
                    weights=list(self.regions.values())
                )[0],
                "ltv_percent": random.randint(60, 90),
                "loan_amount": loan_amount,
                "disbursed_date": loan_date.strftime("%m/%d/%Y"),
                "interest_rate_percent": interest_rate,
                "term_months": term_months,
                "monthly_payment": monthly_payment,
                "payments_made": payments_made,
                "outstanding_balance": outstanding_balance,
                "status": status,
                "email": self.generate_email(client_name)
            }
            clients.append(client)

        # Sort by client_id
        clients.sort(key=lambda x: x["client_id"])

        return clients

    def generate_recent_transactions(self, count: int = 15) -> List[Dict[str, Any]]:
        """Generate recent loan transactions."""
        transactions = []
        start_date = datetime.now() - timedelta(days=180)

        for i in range(count):
            # Generate transaction date
            days_ago = random.randint(0, 180)
            transaction_date = start_date + timedelta(days=days_ago)

            # Determine loan status
            is_late = random.random() < 0.10  # 10% late payment rate

            transaction = {
                "#": i + 1,
                "loan_id": f"L{str(random.randint(1, 99)).zfill(3)}",
                "client_name": self.generate_client_name(),
                "property_type": random.choice(self.property_types),
                "ltv_percent": random.randint(60, 90),
                "disbursed_date": transaction_date.strftime("%m/%d/%Y"),
                "loan_amount": random.randint(15_000_000, 300_000_000),
                "status": "Late Payment" if is_late else "Active"
            }
            transactions.append(transaction)

        # Sort by disbursed date (most recent first)
        transactions.sort(key=lambda x: datetime.strptime(x["disbursed_date"], "%m/%d/%Y"),
                         reverse=True)

        # Renumber after sorting
        for i, trans in enumerate(transactions):
            trans["#"] = i + 1

        return transactions

    def generate_high_risk_profiles(self) -> List[Dict[str, Any]]:
        """Generate high-risk client profiles."""
        profiles = []

        high_risk_clients = [
            {"name": "Bender-Brown", "loan_id": "L086", "ltv": 83,
             "email": "april72@smith.biz", "risk_level": 95},
            {"name": "Chavez & Morgan", "loan_id": "L076", "ltv": 83,
             "email": "hmcpherson@hotmail.com", "risk_level": 85},
            {"name": "Mitchell-Anderson", "loan_id": None, "ltv": None,
             "email": None, "risk_level": 75},
            {"name": "Chavez & Morgan", "loan_id": None, "ltv": None,
             "email": None, "risk_level": 60},
            {"name": "Klein Group", "loan_id": None, "ltv": None,
             "email": None, "risk_level": 55},
            {"name": "Flores Inc", "loan_id": None, "ltv": None,
             "email": None, "risk_level": 50},
            {"name": "Bender-Brown", "loan_id": None, "ltv": None,
             "email": None, "risk_level": 45}
        ]

        for client in high_risk_clients:
            profile = {
                "client_name": client["name"],
                "loan_id": client["loan_id"],
                "ltv_percent": client["ltv"],
                "email": client["email"],
                "risk_score": client["risk_level"]
            }
            profiles.append(profile)

        return profiles

    def generate_portfolio_overview(self) -> Dict[str, Any]:
        """Generate portfolio overview metrics."""
        total_active_balance = random.randint(2_400_000_000, 2_500_000_000)
        rolling_12m_amount = random.randint(3_500_000_000, 3_700_000_000)

        return {
            "active_loan_balance": {
                "value": total_active_balance,
                "ytd_change_percent": -1  # Down 1% vs PYTD
            },
            "rolling_12m_amount": rolling_12m_amount,
            "average_loan_size": random.randint(125_000_000, 135_000_000),
            "active_clients": 50,
            "total_clients": 60,
            "active_loans": 86,
            "payment_status": {
                "active": 0.76,
                "late_payment": 0.10,
                "paid_off": 0.14
            },
            "clients_by_region": self.regions
        }

    def generate_monthly_trends(self) -> List[Dict[str, Any]]:
        """Generate 12-month trend data."""
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        trends = []
        base_amount = 100_000_000

        for i, month in enumerate(months):
            # Create spike in May
            if month == "May":
                amount = 882_900_000
            elif month in ["Feb", "Mar"]:
                amount = random.randint(9_000_000, 10_000_000)
            elif month in ["Apr", "Jun", "Jul"]:
                amount = random.randint(100_000_000, 200_000_000)
            elif month in ["Aug", "Sep", "Oct"]:
                amount = random.randint(300_000_000, 450_000_000)
            elif month == "Nov":
                amount = random.randint(400_000_000, 500_000_000)
            else:
                amount = base_amount + random.randint(-50_000_000, 50_000_000)

            trends.append({
                "month": month,
                "amount": amount,
                "year": 2024 if i < 7 else 2025
            })

        return trends

    def generate_property_type_analytics(self) -> Dict[str, Any]:
        """Generate property type distribution and analytics."""

        # Property type distribution
        distribution = {
            "Apartment Block": 0.24,
            "Retail Mall": 0.23,
            "Mixed-Use": 0.19,
            "Warehouse": 0.17,
            "Office Space": 0.17
        }

        # Year-over-year changes by property type
        ytd_changes = {
            "Retail Mall": {"change_percent": 17, "loans_2023": 6, "loans_2024": 7},
            "Apartment Block": {"change_percent": 14, "loans_2023": 7, "loans_2024": 8},
            "Office Space": {"change_percent": 0, "loans_2023": 4, "loans_2024": 4},
            "Warehouse": {"change_percent": -40, "loans_2023": 5, "loans_2024": 3},
            "Mixed-Use": {"change_percent": -78, "loans_2023": 9, "loans_2024": 2}
        }

        # Average loan size by property type
        avg_loan_sizes = {
            "Mixed-Use": 173_000_000,
            "Apartment Block": 158_000_000,
            "Office Space": 148_000_000,
            "Warehouse": 138_000_000,
            "Retail Mall": 132_000_000
        }

        # Average metrics across all property types
        avg_metrics = {
            "avg_ltv": 0.74,
            "avg_interest_rate": 0.12,
            "avg_term_months": 63
        }

        return {
            "distribution": distribution,
            "ytd_changes": ytd_changes,
            "avg_loan_sizes": avg_loan_sizes,
            "avg_metrics": avg_metrics
        }

    def generate_all_data(self) -> Dict[str, Any]:
        """Generate complete dataset for the dashboard."""
        return {
            "generated_at": datetime.now().isoformat(),
            "recent_transactions": self.generate_recent_transactions(15),
            "high_risk_profiles": self.generate_high_risk_profiles(),
            "portfolio_overview": self.generate_portfolio_overview(),
            "monthly_trends": self.generate_monthly_trends(),
            "property_analytics": self.generate_property_type_analytics()
        }

    def save_to_json(self, filename: str = "lendsight_data.json"):
        """Generate and save all data to a JSON file."""
        data = self.generate_all_data()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")
        return data

    def export_clients_to_csv(self, filename: str = "clients_data.csv", count: int = 100):
        """Export client data to a single CSV file."""
        clients = self.generate_clients(count)

        with open(filename, 'w', newline='') as f:
            fieldnames = [
                'client_id', 'client_name', 'loan_id', 'property_type', 'region',
                'ltv_percent', 'loan_amount', 'disbursed_date', 'interest_rate_percent',
                'term_months', 'monthly_payment', 'payments_made', 'outstanding_balance',
                'status', 'email'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(clients)

        print(f"✓ Exported {count} clients to: {filename}")

        # Calculate and display active loan balance summary
        active_balance = sum(
            client['outstanding_balance']
            for client in clients
            if client['status'] in ['Active', 'Late Payment']
        )
        print(f"  Total Active Loan Balance: ${active_balance:,.2f}")

        return clients

    def export_to_csv(self, output_dir: str = "lendsight_csv"):
        """Export all data to CSV files."""
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        data = self.generate_all_data()

        # 1. Export Recent Transactions
        transactions_file = os.path.join(output_dir, "recent_transactions.csv")
        with open(transactions_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                '#', 'loan_id', 'client_name', 'property_type',
                'ltv_percent', 'disbursed_date', 'loan_amount', 'status'
            ])
            writer.writeheader()
            writer.writerows(data['recent_transactions'])
        print(f"✓ Exported: {transactions_file}")

        # 2. Export High Risk Profiles
        risk_file = os.path.join(output_dir, "high_risk_profiles.csv")
        with open(risk_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'client_name', 'loan_id', 'ltv_percent', 'email', 'risk_score'
            ])
            writer.writeheader()
            writer.writerows(data['high_risk_profiles'])
        print(f"✓ Exported: {risk_file}")

        # 3. Export Portfolio Overview
        portfolio_file = os.path.join(output_dir, "portfolio_overview.csv")
        with open(portfolio_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Metric', 'Value'])
            po = data['portfolio_overview']
            writer.writerow(['Active Loan Balance', po['active_loan_balance']['value']])
            writer.writerow(['YTD Change %', po['active_loan_balance']['ytd_change_percent']])
            writer.writerow(['12-Month Rolling Amount', po['rolling_12m_amount']])
            writer.writerow(['Average Loan Size', po['average_loan_size']])
            writer.writerow(['Active Clients', po['active_clients']])
            writer.writerow(['Total Clients', po['total_clients']])
            writer.writerow(['Active Loans', po['active_loans']])
            writer.writerow(['Payment Status - Active %', po['payment_status']['active']])
            writer.writerow(['Payment Status - Late %', po['payment_status']['late_payment']])
            writer.writerow(['Payment Status - Paid Off %', po['payment_status']['paid_off']])
        print(f"✓ Exported: {portfolio_file}")

        # 4. Export Regional Distribution
        region_file = os.path.join(output_dir, "clients_by_region.csv")
        with open(region_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Region', 'Percentage'])
            for region, pct in data['portfolio_overview']['clients_by_region'].items():
                writer.writerow([region, pct])
        print(f"✓ Exported: {region_file}")

        # 5. Export Monthly Trends
        trends_file = os.path.join(output_dir, "monthly_trends.csv")
        with open(trends_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['month', 'year', 'amount'])
            writer.writeheader()
            writer.writerows(data['monthly_trends'])
        print(f"✓ Exported: {trends_file}")

        # 6. Export Property Type Distribution
        dist_file = os.path.join(output_dir, "property_type_distribution.csv")
        with open(dist_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Property Type', 'Percentage'])
            for prop_type, pct in data['property_analytics']['distribution'].items():
                writer.writerow([prop_type, pct])
        print(f"✓ Exported: {dist_file}")

        # 7. Export Property Type YTD Changes
        ytd_file = os.path.join(output_dir, "property_type_ytd_changes.csv")
        with open(ytd_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Property Type', 'Change %', 'Loans 2023', 'Loans 2024'])
            for prop_type, changes in data['property_analytics']['ytd_changes'].items():
                writer.writerow([
                    prop_type,
                    changes['change_percent'],
                    changes['loans_2023'],
                    changes['loans_2024']
                ])
        print(f"✓ Exported: {ytd_file}")

        # 8. Export Average Loan Sizes by Property Type
        avg_sizes_file = os.path.join(output_dir, "avg_loan_sizes_by_type.csv")
        with open(avg_sizes_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Property Type', 'Average Loan Size'])
            for prop_type, avg_size in data['property_analytics']['avg_loan_sizes'].items():
                writer.writerow([prop_type, avg_size])
        print(f"✓ Exported: {avg_sizes_file}")

        # 9. Export Property Analytics Averages
        avg_metrics_file = os.path.join(output_dir, "property_avg_metrics.csv")
        with open(avg_metrics_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Metric', 'Value'])
            metrics = data['property_analytics']['avg_metrics']
            writer.writerow(['Average LTV', metrics['avg_ltv']])
            writer.writerow(['Average Interest Rate', metrics['avg_interest_rate']])
            writer.writerow(['Average Term (months)', metrics['avg_term_months']])
        print(f"✓ Exported: {avg_metrics_file}")

        return data

    def print_summary(self, data: Dict[str, Any]):
        """Print a summary of the generated data."""
        print("\n" + "="*60)
        print("LENDSIGHT DATA GENERATION SUMMARY")
        print("="*60)

        print(f"\n📊 Portfolio Overview:")
        po = data['portfolio_overview']
        print(f"  Active Loan Balance: ${po['active_loan_balance']['value']:,}")
        print(f"  12-Month Rolling: ${po['rolling_12m_amount']:,}")
        print(f"  Average Loan Size: ${po['average_loan_size']:,}")
        print(f"  Active Clients: {po['active_clients']}/{po['total_clients']}")
        print(f"  Active Loans: {po['active_loans']}")

        print(f"\n📋 Recent Transactions: {len(data['recent_transactions'])} generated")

        print(f"\n⚠️  High Risk Profiles: {len(data['high_risk_profiles'])} clients")

        print(f"\n🏢 Property Types:")
        for prop_type, percent in data['property_analytics']['distribution'].items():
            print(f"  {prop_type}: {percent*100:.0f}%")

        print(f"\n📈 Monthly Trends: {len(data['monthly_trends'])} months")

        print("\n" + "="*60)


def main():
    """Main execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate LendSight Real Estate Finance Data"
    )
    parser.add_argument(
        '--format',
        choices=['json', 'csv', 'both', 'clients'],
        default='both',
        help='Output format: json, csv, both, or clients (default: both)'
    )
    parser.add_argument(
        '--csv-dir',
        default='lendsight_csv',
        help='Directory for CSV files (default: lendsight_csv)'
    )
    parser.add_argument(
        '--json-file',
        default='lendsight_data.json',
        help='JSON output file (default: lendsight_data.json)'
    )
    parser.add_argument(
        '--clients-file',
        default='clients_data.csv',
        help='CSV file for client data (default: clients_data.csv)'
    )
    parser.add_argument(
        '--client-count',
        type=int,
        default=100,
        help='Number of clients to generate (default: 100)'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed for reproducibility (default: 42)'
    )

    args = parser.parse_args()

    print("Generating LendSight Real Estate Finance Data...")
    print(f"Random seed: {args.seed}\n")

    # Create generator
    generator = LendSightDataGenerator(seed=args.seed)

    data = None

    # Generate clients data
    if args.format == 'clients':
        print(f"\n📊 Generating {args.client_count} clients...")
        clients = generator.export_clients_to_csv(args.clients_file, args.client_count)
        print(f"\n✅ Client data generation complete!")
        print(f"\nGenerated {len(clients)} clients")
        print(f"CSV file: {args.clients_file}")
        return

    # Generate based on format
    if args.format in ['json', 'both']:
        print(f"\n📄 Generating JSON output...")
        data = generator.save_to_json(args.json_file)

    if args.format in ['csv', 'both']:
        print(f"\n📊 Generating CSV outputs...")
        data = generator.export_to_csv(args.csv_dir)
        print(f"\n✓ All CSV files exported to '{args.csv_dir}/' directory")

    # Print summary if data was generated
    if data:
        generator.print_summary(data)

    print("\n✅ Data generation complete!")

    if args.format == 'json':
        print(f"\nJSON file: {args.json_file}")
    elif args.format == 'csv':
        print(f"\nCSV files: {args.csv_dir}/")
    else:
        print(f"\nJSON file: {args.json_file}")
        print(f"CSV files: {args.csv_dir}/")


if __name__ == "__main__":
    main()
