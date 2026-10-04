    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║   ███████╗ ██████╗ ██████╗ ████████╗██╗ ██████╗  █████╗ ████████╗███████╗   ║
    ║   ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██║██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝   ║
    ║   █████╗  ██║   ██║██████╔╝   ██║   ██║██║  ███╗███████║   ██║   █████╗     ║
    ║   ██╔══╝  ██║   ██║██╔══██╗   ██║   ██║██║   ██║██╔══██║   ██║   ██╔══╝     ║
    ║   ██║     ╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║  ██║   ██║   ███████╗   ║
    ║   ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝   ║
    ║                                                                             ║
    ║      ██████╗ ███████╗██╗     ███████╗███████╗███╗   ██╗                     ║
    ║      ██╔══██╗██╔════╝██║     ██╔════╝██╔════╝████╗  ██║                     ║
    ║      ██████╔╝█████╗  ██║     ███████╗█████╗  ██╔██╗ ██║                     ║
    ║      ██╔══██╗██╔══╝  ██║     ╚════██║██╔══╝  ██║╚██╗██║                     ║
    ║      ██████╔╝███████╗███████╗███████║███████╗██║ ╚████║                     ║
    ║      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝                     ║
    ║                                                                             ║
    ║      ██╗     ███████╗ █████╗ ██╗  ██╗                                       ║
    ║      ██║     ██╔════╝██╔══██╗██║ ██╔╝                                       ║
    ║      ██║     █████╗  ███████║█████╔╝                                        ║
    ║      ██║     ██╔══╝  ██╔══██║██╔═██╗                                        ║
    ║      ███████╗███████╗██║  ██║██║  ██╗                                       ║
    ║      ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                                       ║
    ║                                                                             ║
    ║                    Configuration Leak Tracker                               ║
    ╚═════════════════════════════════════════════════════════════════════════════╝

# Fortigate Belsen Leak Research

## Fork Provenance

> [!IMPORTANT]
> This repository is a GitHub fork of `arsolutioner/fortigate-belsen-leak`.
>
> - **Original source:** `arsolutioner/fortigate-belsen-leak`
> - **Original authorship:** upstream project authors and contributors
> - **Local purpose:** defensive security research and analysis of the publicly disclosed dataset
> - **Observed local additions:** `affected_ips_no_ports.txt` was added in commit `f96aab82bfe05c92832ebbd98c075586b1acbfa3`; `ips_results_countries.xlsx` was added in commit `dc99b5ef08df6bce81e8ac0da29cd913880fce12`
> - **Sync state:** the local fork has diverged from upstream. No automatic upstream-tracking claim is made.
> - **License:** MIT. See `LICENSE`.

This repository contains informaion about the Fortigate firewall vulnerability (CVE-2022-40684) and affected IPs that were publicly disclosed by the Belsen Group. This information is being shared for security research and defensive purposes to help organizations identify if they were impacted.

## Background

In 2022, Fortinet disclosed a critical authentication bypass vulnerability (CVE-2022-40684) affecting FortiOS, FortiProxy, and FortiSwitchManager. In January 2025, configurations from approximately 15,000 affected devices were publicly released by the Belsen Group.

## Purpose

This repository serves as a resource for:
- Security researchers studying the impact of CVE-2022-40684
- Organizations to check if they were affected
- Raising awareness about the importance of timely security patches

## Contents

- `affected_ips.txt`: upstream list of IP addresses identified in the disclosed dataset
- `affected_ips_no_ports.txt`: local derived list added after the fork was created
- `ips_results_countries.xlsx`: local derived workbook added after the fork was created
- `REFERENCES.md`: background references

## Data Provenance and Limitations

- The repository is a historical research snapshot around the January 2025 disclosure. It is **not** a live exposure feed.
- An IP address appearing in the dataset does not prove that the current IP owner is compromised, still vulnerable, or even the same organization that used the address at the time of the disclosure.
- IP ownership, hosting assignments, NAT, cloud resources, and device lifecycle can change. Current exposure must be validated independently.
- The generation methodology for the two local derived files is not documented in the repository. Treat them as convenience research artifacts rather than a separate authoritative source.
- Do not use this dataset alone to make attribution, incident-severity, customer-impact, or remediation decisions.
- Do not add raw leaked configurations, credentials, private keys, or other sensitive material to this repository.

## Disclaimer

This information is provided for defensive security research purposes only. The data has been publicly disclosed and is being shared to help organizations assess their exposure and take necessary remediation steps.

## References

- [Fortinet Advisory](https://www.fortinet.com/blog/psirt-blogs/update-regarding-cve-2022-40684)
- CVE-2022-40684
