import argparse
import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class BuildReport:
    total_time_ms: int
    cache_hits: int
    cache_misses: int
    worker_count: int

def generate_report(total_time_ms: int, cache_hits: int, cache_misses: int, worker_count: int) -> BuildReport:
    return BuildReport(total_time_ms, cache_hits, cache_misses, worker_count)

def write_report(report: BuildReport, report_path: str = 'build-report.json') -> None:
    with open(report_path, 'w') as f:
        json.dump({
            'total_time_ms': report.total_time_ms,
            'cache_hits': report.cache_hits,
            'cache_misses': report.cache_misses,
            'worker_count': report.worker_count
        }, f, indent=4)

def main() -> None:
    parser = argparse.ArgumentParser(description='SWC-Booster report generator')
    parser.add_argument('--report-path', help='Custom output location for the report', default='build-report.json')
    parser.add_argument('--json', action='store_true', help='Generate report in JSON format')
    parser.add_argument('--total-time-ms', type=int, help='Total build time in milliseconds', required=True)
    parser.add_argument('--cache-hits', type=int, help='Number of cache hits', required=True)
    parser.add_argument('--cache-misses', type=int, help='Number of cache misses', required=True)
    parser.add_argument('--worker-count', type=int, help='Number of workers', required=True)
    args = parser.parse_args()

    if args.json:
        report = generate_report(args.total_time_ms, args.cache_hits, args.cache_misses, args.worker_count)
        write_report(report, args.report_path)

if __name__ == '__main__':
    main()
