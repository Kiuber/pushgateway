# Prometheus Pushgateway(with Time To Live)

The Prometheus Pushgateway exists to allow ephemeral and batch jobs to
expose their metrics to Prometheus. Since these kinds of jobs may not
exist long enough to be scraped, they can instead push their metrics
to a Pushgateway. The Pushgateway then exposes these metrics to
Prometheus.

Additionally to promethues pushgateway it address the issue [prometheus/pushgateway#117](https://github.com/prometheus/pushgateway/issues/117)

### Using Docker

You can deploy the Pushgateway using the [dmathai/prom-pushgateway-ttl](https://hub.docker.com/r/dmathai/prom-pushgateway-ttl/) Docker image.

For example:

```bash
docker pull dmathai/prom-pushgateway-ttl:latest

docker run -d -p 9091:9091 dmathai/prom-pushgateway-ttl:latest --metric.timetolive=60s
```

## Use it

### Time To Live
If we pass a argument `metric.timetolive` at the time of start up(Example : `--metric.timetolive=60s`), 
the metrics will be removed from pushgateway after the 'metric.timetolive' from the time of pushing the metric.
**The clean up jobs runs every 60 sec. So anything below 60 sec will not work.** 
