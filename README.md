# ZeroMOUSE Home Assistant Integration

> [!IMPORTANT]
>
> This repository only holds my investigation into the ZeroMOUSE API back in 2024: [docs/2024-10-api](https://github.com/siku2/hass-zeromouse/tree/main/docs/2024-10-api).
> I never ended up writing the full integration due to other projects coming up.
>
> Now in 2026 I no longer have a need for this project because I've replaced the firmware on the ZeroMOUSE device with my own esphome-based one.
> All my work is public so if you're interested and know where to look you will find it, but I'm not going to advertise it loudly just yet.
>
> If you want the cloud integration approach consider some other projects (I haven't tested any of them so don't take this as an endorsement). You can find here: https://github.com/topics/zeromouse

[![GitHub Release](https://img.shields.io/github/release/siku2/hass-zeromouse.svg?style=flat-square)](https://github.com/siku2/hass-zeromouse/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg?style=flat-square)](https://hacs.xyz/docs/faq/custom_repositories)

[![License](https://img.shields.io/github/license/siku2/hass-zeromouse.svg?style=flat-square)](LICENSE)
[![GitHub Activity](https://img.shields.io/github/commit-activity/y/siku2/hass-zeromouse.svg?style=flat-square)](https://github.com/siku2/hass-zeromouse/commits/main)



_short explanation_

## Installation

Make sure you have [HACS](https://hacs.xyz) installed.

1. Add this repository as a custom repository to HACS: [![Add Repository](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=siku2&repository=hass-zeromouse&category=integration)
2. Use HACS to install the integration.
3. Restart Home Assistant.
4. Set up the integration using the UI: [![Add Integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=zeromouse)

## Contributions are welcome

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

### Providing translations for other languages

[![GitLocalize](https://gitlocalize.com/repo/$GIT_LOCALIZE_PROJECT/whole_project/badge.svg)](https://gitlocalize.com/repo/$GIT_LOCALIZE_PROJECT)

If you would like to use the integration in another language, you can help out by providing the necessary translations.

[Head over to **GitLocalize** to start translating.](https://gitlocalize.com/repo/$GIT_LOCALIZE_PROJECT)

If your desired language isn't available there, just open an issue to request it.

You can also just do the translations manually in [custom_components/zeromouse/translations/](./custom_components/zeromouse/translations/) and open a pull request with the changes.
