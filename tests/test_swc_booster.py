import json
from swc_booster import generate_report, write_report
import pytest
import os

def test_generate_report():
    report = generate_report(1000, 10, 5, 2)
    assert report.total_time_ms == 1000
    assert report.cache_hits == 10
    assert report.cache_misses == 5
    assert report.worker_count == 2

def test_write_report(tmp_path):
    report = generate_report(1000, 10, 5, 2)
    report_path = tmp_path / 'build-report.json'
    write_report(report, str(report_path))
    with open(report_path, 'r') as f:
        data = json.load(f)
        assert data['total_time_ms'] == 1000
        assert data['cache_hits'] == 10
        assert data['cache_misses'] == 5
        assert data['worker_count'] == 2

def test_write_report_custom_path(tmp_path):
    report = generate_report(1000, 10, 5, 2)
    report_path = tmp_path / 'custom-report.json'
    write_report(report, str(report_path))
    assert os.path.exists(report_path)

def test_main(tmp_path, monkeypatch):
    monkeypatch.setenv('PYTHONPATH', str(tmp_path))
    report_path = tmp_path / 'build-report.json'
    monkeypatch.setattr('sys.argv', ['swc-booster', '--json', '--report-path', str(report_path), '--total-time-ms', '1000', '--cache-hits', '10', '--cache-misses', '5', '--worker-count', '2'])
    from swc_booster import main
    main()
    assert os.path.exists(report_path)
    with open(report_path, 'r') as f:
        data = json.load(f)
        assert data['total_time_ms'] == 1000
        assert data['cache_hits'] == 10
        assert data['cache_misses'] == 5
        assert data['worker_count'] == 2
