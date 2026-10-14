# Performance Analyzer Edge Cases

- Empty input should produce a clear empty-state message.
- A single student's report should calculate without special-case errors.
- Missing marks should not silently become zero unless configured.
- Tied averages should follow a documented ranking rule.
- Reject non-numeric scores and values outside the accepted range.