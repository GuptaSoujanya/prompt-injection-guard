import argparse
from .detectors import PromptInjectionDetector
from .benchmark import SafetyBenchmarkRunner

def main():
    parser = argparse.ArgumentParser(
        prog="prompt-guard",
        description="prompt-injection-guard: Red-teaming and prompt defense benchmark."
    )
    parser.add_argument("--scan", type=str, help="Single prompt string to scan for adversarial injection")
    parser.add_argument("--benchmark", action="store_true", help="Run standard red-teaming benchmark evaluation")

    args = parser.parse_args()

    detector = PromptInjectionDetector()

    if args.scan:
        res = detector.analyze(args.scan)
        print("\n" + "="*50)
        print("          PROMPT SECURITY AUDIT")
        print("="*50)
        print(f" Prompt     : {args.scan}")
        print(f" Status     : {'[THREAT DETECTED]' if res.is_threat else '[SAFE]'}")
        print(f" Confidence : {res.confidence * 100:.1f}%")
        if res.detected_patterns:
            print(f" Patterns   : {', '.join(res.detected_patterns)}")
        print("="*50 + "\n")
        return

    # Default to benchmark run
    runner = SafetyBenchmarkRunner(detector)
    report = runner.run_benchmark()

    print("\n" + "="*50)
    print("      SAFETY BENCHMARK EVALUATION REPORT")
    print("="*50)
    print(f" Total Probes Evaluated  : {report['total_samples']}")
    print(f" Adversarial Detection   : {report['detection_recall'] * 100:.1f}%")
    print(f" Attack Success Rate     : {report['attack_success_rate'] * 100:.1f}%")
    print(f" False Positive Rate     : {report['false_positive_rate'] * 100:.1f}%")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
