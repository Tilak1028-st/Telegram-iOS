#new_pod_repository(
#    name = "Web3Auth",
#    url = "https://github.com/Web3Auth/web3auth-swift-sdk/archive/refs/tags/9.0.0.zip",
#    podspec_url = "Vendor/Podspec/Web3Auth.podspec",
#    is_xcframework = True,
#    generate_module_map = True,
#    generate_header_map = True,
#)


new_pod_repository(
    name = "BigInt",
    url = "https://github.com/attaswift/BigInt/archive/refs/tags/v5.4.1.zip",
    podspec_url = "Vendor/Podspec/BigInt.podspec",
    generate_header_map = 1,
)
